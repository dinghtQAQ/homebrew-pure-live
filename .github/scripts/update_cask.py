#!/usr/bin/env python3
"""Refresh the pure-live cask from the latest upstream GitHub release."""

import hashlib
import json
import re
import urllib.request
from pathlib import Path

REPO = "liuchuancong/pure_live"
CASK = Path("Casks/pure-live.rb")
ASSET_RE = re.compile(r"^PureLive-(.+)-(\d+)-macos-universal\.zip$")


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "dinghtQAQ-homebrew-pure-live",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def main() -> None:
    release = fetch_json(f"https://api.github.com/repos/{REPO}/releases/latest")
    tag = release["tag_name"].removeprefix("v")
    asset = next(
        item for item in release["assets"] if ASSET_RE.match(item["name"])
    )
    match = ASSET_RE.match(asset["name"])
    assert match is not None
    version, build = match.group(1), match.group(2)
    if version != tag:
        raise SystemExit(f"asset version {version} does not match tag {tag}")

    digest = asset.get("digest", "")
    if digest.startswith("sha256:"):
        sha256 = digest.removeprefix("sha256:")
    else:
        print("release digest missing; downloading asset", flush=True)
        with urllib.request.urlopen(asset["browser_download_url"], timeout=300) as response:
            hasher = hashlib.sha256()
            while chunk := response.read(1024 * 1024):
                hasher.update(chunk)
        sha256 = hasher.hexdigest()

    cask = CASK.read_text()
    updated = re.sub(r'version "[^"]+"', f'version "{version},{build}"', cask, count=1)
    updated = re.sub(r'sha256 "[^"]+"', f'sha256 "{sha256}"', updated, count=1)
    if updated == cask:
        print(f"already at {version},{build}")
        return

    CASK.write_text(updated)
    print(f"updated to {version},{build} sha256={sha256}")


if __name__ == "__main__":
    main()

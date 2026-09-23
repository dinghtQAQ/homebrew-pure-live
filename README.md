# dinghtQAQ/pure-live

Homebrew cask for [纯粹直播 / Pure Live](https://github.com/liuchuancong/pure_live).

The upstream macOS archive name includes a build number that is not part of the Git tag. This tap tracks the latest GitHub release and rewrites the cask, so a normal `brew upgrade` can install it.

## Install

```sh
brew tap dinghtqaq/pure-live
brew install --cask pure-live
```

Homebrew 4.6 and later refuses to load a third-party tap until you trust it:

```sh
brew trust dinghtqaq/pure-live
```

If `/Applications/纯粹直播.app` was installed by hand, install with `--force` so Homebrew can replace it:

```sh
brew install --cask --force pure-live
```

## Update

```sh
brew update
brew upgrade --cask pure-live
```

A scheduled workflow checks the upstream release every hour and commits a new cask version when one is published. After `brew update`, `brew upgrade --cask pure-live` replaces the app.

The current package is ad-hoc signed. macOS may ask you to allow it in System Settings → Privacy & Security the first time it opens.

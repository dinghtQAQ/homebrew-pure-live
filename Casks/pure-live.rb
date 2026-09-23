cask "pure-live" do
  version "3.1.4,4103"
  sha256 "f302d1b220ce1a51fa40e0d1ac3927e4b77490a505c5aa86a5559e92c30a3460"

  url "https://github.com/liuchuancong/pure_live/releases/download/v#{version.csv.first}/PureLive-#{version.csv.first}-#{version.csv.second}-macos-universal.zip"
  name "纯粹直播"
  desc "Third-party multi-platform live stream aggregator"
  homepage "https://github.com/liuchuancong/pure_live"

  livecheck do
    url "https://api.github.com/repos/liuchuancong/pure_live/releases/latest"
    strategy :json do |json|
      tag = json["tag_name"]&.delete_prefix("v")
      asset = json["assets"]&.find { |item| item["name"]&.end_with?("macos-universal.zip") }
      build = asset&.dig("name")&.[](/PureLive-#{Regexp.escape(tag.to_s)}-(\d+)-macos-universal\.zip/, 1)
      next if tag.blank? || build.blank?

      "#{tag},#{build}"
    end
  end

  depends_on macos: :monterey

  app "纯粹直播.app"

  zap trash: [
    "~/Library/Containers/com.mystyle.purelive",
    "~/Library/Containers/com.mystyle.pureLive",
  ]
end

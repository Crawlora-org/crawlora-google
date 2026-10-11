require_relative "lib/crawlora/google/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-google"
  spec.version = Crawlora::Google::VERSION
  spec.summary = "Google API client for Crawlora (40 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Google API. Covers Maps search, places, reviews and photos; News; Trends; Finance quotes and markets; suggestions; videos; and jobs across 40 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-google", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-google/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end

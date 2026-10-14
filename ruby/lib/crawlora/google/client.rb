require "json"
require "net/http"
require "uri"

module Crawlora
  module Google
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"google-finance-analyst-articles": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-analyst-articles", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/analyst-articles/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-chart": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-chart", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}, {"description": "Window: 1d, 5d, 1m, 6m, ytd, 1y, 5y, max", "in": "query", "name": "window", "type": "string"}], "path": "/google/finance/chart/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "window", "type": "string"}], "security": ["ApiKeyAuth"]}, "google-finance-classification": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-classification", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/classification/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-company": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-company", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/company/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-context": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-context", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "apple"}], "path": "/google/finance/context", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "google-finance-financials": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-financials", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/financials/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-category-news": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-category-news", "method": "GET", "params": [{"description": "Google Finance category id", "in": "path", "name": "category", "required": true, "type": "string", "x-example": "2"}, {"description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/google/finance/markets/categories/{category}/news", "pathParams": ["category"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-category-stocks": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-category-stocks", "method": "GET", "params": [{"description": "Google Finance category id", "in": "path", "name": "category", "required": true, "type": "string", "x-example": "2"}, {"description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/google/finance/markets/categories/{category}/stocks", "pathParams": ["category"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-earnings": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-earnings", "method": "GET", "params": [], "path": "/google/finance/markets/earnings", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-featured": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-featured", "method": "GET", "params": [], "path": "/google/finance/markets/featured", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-headline": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-headline", "method": "GET", "params": [], "path": "/google/finance/markets/headline", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-indices": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-indices", "method": "GET", "params": [], "path": "/google/finance/markets/indices", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-movers": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-movers", "method": "GET", "params": [{"description": "Comma-separated numeric categories", "in": "query", "name": "categories", "type": "string"}, {"description": "Result count", "in": "query", "name": "count", "type": "integer"}, {"description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/google/finance/markets/movers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "categories", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-top": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-top", "method": "GET", "params": [{"description": "Google Finance metric id", "in": "query", "name": "metric", "type": "integer"}, {"description": "Page number", "in": "query", "name": "page", "type": "integer"}], "path": "/google/finance/markets/top", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "metric", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-trending": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-trending", "method": "GET", "params": [{"description": "Result limit", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/finance/markets/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-news": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-news", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}, {"description": "Article limit", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/finance/news/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-quote": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-quote", "method": "GET", "params": [{"description": "Stock symbol to fetch the latest quote for (e.g., AAPL:NASDAQ, BTC-USD)", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/quote/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-related": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-related", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/related/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-search": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-search", "method": "GET", "params": [{"description": "Keyword to search for (e.g., Apple)", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Apple"}], "path": "/google/finance/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "google-finance-ticker": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-ticker", "method": "GET", "params": [{"description": "Ticker symbol to fetch data for example:AAPL:NASDAQ, BTC-USD ", "in": "path", "name": "ticker", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}, {"description": "Time window for the ticker data (default: 1d), options: 1d, 5d, 1m, 6m, 1y, 5y, max", "in": "query", "name": "window", "type": "string"}], "path": "/google/finance/ticker/{ticker}", "pathParams": ["ticker"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "window", "type": "string"}], "security": ["ApiKeyAuth"]}, "google-jobs": {"bodyParam": "option", "bodyRequired": true, "id": "google-jobs", "method": "POST", "params": [{"description": "Google Jobs search payload", "in": "body", "name": "option", "required": true, "schema": {"$ref": "#/definitions/google.JobsOption"}}], "path": "/google/jobs", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-map-place": {"bodyParam": null, "bodyRequired": false, "id": "google-map-place", "method": "GET", "params": [{"description": "Google Place ID", "in": "path", "name": "place_id", "required": true, "type": "string", "x-example": "ChIJs3cv0KuvEmsRHcXYwNJ6GU0"}], "path": "/google/map/place/{place_id}", "pathParams": ["place_id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-map-place-photos": {"bodyParam": null, "bodyRequired": false, "id": "google-map-place-photos", "method": "GET", "params": [{"description": "Google Place ID", "in": "path", "name": "place_id", "required": true, "type": "string", "x-example": "ChIJs3cv0KuvEmsRHcXYwNJ6GU0"}, {"description": "Maximum number of photos to return. Omit or 0 for all captured.", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/map/place/{place_id}/photos", "pathParams": ["place_id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-map-place-reviews": {"bodyParam": null, "bodyRequired": false, "id": "google-map-place-reviews", "method": "GET", "params": [{"description": "Google Place ID", "in": "path", "name": "place_id", "required": true, "type": "string", "x-example": "ChIJs3cv0KuvEmsRHcXYwNJ6GU0"}, {"description": "Maximum number of reviews to return. Omit or 0 for all captured.", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/map/place/{place_id}/reviews", "pathParams": ["place_id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-map-search": {"bodyParam": "mapSearchOption", "bodyRequired": true, "id": "google-map-search", "method": "POST", "params": [{"description": "Search options", "in": "body", "name": "mapSearchOption", "required": true, "schema": {"$ref": "#/definitions/google.MapSearchOption"}}], "path": "/google/map/search", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-news": {"bodyParam": null, "bodyRequired": false, "id": "google-news", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "1-based page within the current finite result snapshot; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer", "x-example": 1}, {"description": "Results per page; defaults to 10, clamped to 1..50", "in": "query", "maximum": 50, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Two-letter country code; defaults to us", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Google UI language; defaults to en", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/google/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "google-news-search": {"bodyParam": "searchOption", "bodyRequired": true, "id": "google-news-search", "method": "POST", "params": [{"description": "Search options; keyword, language and country are required. limit defaults to 10 and is clamped to 10..100; page defaults to 1.", "in": "body", "name": "searchOption", "required": true, "schema": {"$ref": "#/definitions/google.SearchOption"}}], "path": "/google/news", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-suggest": {"bodyParam": null, "bodyRequired": false, "id": "google-suggest", "method": "GET", "params": [{"description": "Search query prefix", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "Suggestions to return; defaults to 10, clamped to 1..12", "in": "query", "maximum": 12, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Google result country; defaults to us", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Google UI language; defaults to en", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": "web", "description": "Suggestion source; defaults to web", "enum": ["web", "youtube", "shopping"], "in": "query", "name": "source", "type": "string"}, {"description": "Add Google's type, relevance score, and description to each suggestion; defaults to false", "in": "query", "name": "rich", "type": "boolean", "x-example": false}], "path": "/google/suggest", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"enum": ["web", "youtube", "shopping"], "in": "query", "name": "source", "type": "string"}, {"in": "query", "name": "rich", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "google-trends-categories": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-categories", "method": "GET", "params": [], "path": "/google/trends/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-enums": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-enums", "method": "GET", "params": [], "path": "/google/trends/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-interest-by-region": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-interest-by-region", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/interest-by-region", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-interest-over-time": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-interest-over-time", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/interest-over-time", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-related-topics": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-related-topics", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/related-topics", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-rising-queries": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-rising-queries", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/rising-queries", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-top-queries": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-top-queries", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/top-queries", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-locations": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-locations", "method": "GET", "params": [], "path": "/google/trends/locations", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-trending": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-trending", "method": "GET", "params": [{"default": "US", "description": "Country/territory location code", "enum": ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "IO", "VG", "BN", "BG", "BF", "BI", "KH", "CM", "CA", "CV", "BQ", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "XK", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "KP", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "KR", "SS", "ES", "LK", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UM", "VI", "UG", "UA", "AE", "GB", "US", "UY", "UZ", "VU", "VA", "VE", "VN", "WF", "EH", "YE", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string"}, {"default": "en-US", "description": "Google Trends UI locale", "in": "query", "name": "hl", "type": "string"}, {"default": 0, "description": "Timezone offset minutes", "in": "query", "name": "tz", "type": "integer"}, {"default": "24h", "description": "Trend window", "enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "window", "type": "string"}, {"description": "Alias for window", "enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "time_range", "type": "string"}, {"default": 0, "description": "Trending category id", "enum": [0, 3, 47, 44, 22, 12, 5, 7, 71, 8, 45, 65, 11, 13, 958, 19, 16, 299, 14, 66, 29, 533, 174, 18, 20, 67], "in": "query", "name": "category", "type": "integer"}, {"default": "all", "description": "Trend status filter", "enum": ["all", "active", "ended"], "in": "query", "name": "status", "type": "string"}, {"default": "relevance", "description": "Sort mode", "enum": ["relevance", "title", "recency", "search_volume"], "in": "query", "name": "sort_by", "type": "string"}, {"default": 20, "description": "Maximum rows to return", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/trends/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "IO", "VG", "BN", "BG", "BF", "BI", "KH", "CM", "CA", "CV", "BQ", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "XK", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "KP", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "KR", "SS", "ES", "LK", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UM", "VI", "UG", "UA", "AE", "GB", "US", "UY", "UZ", "VU", "VA", "VE", "VN", "WF", "EH", "YE", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string"}, {"in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "tz", "type": "integer"}, {"enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "window", "type": "string"}, {"enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "time_range", "type": "string"}, {"enum": ["0", "3", "47", "44", "22", "12", "5", "7", "71", "8", "45", "65", "11", "13", "958", "19", "16", "299", "14", "66", "29", "533", "174", "18", "20", "67"], "in": "query", "name": "category", "type": "integer"}, {"enum": ["all", "active", "ended"], "in": "query", "name": "status", "type": "string"}, {"enum": ["relevance", "title", "recency", "search_volume"], "in": "query", "name": "sort_by", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-trends-trending-detail": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-trending-detail", "method": "POST", "params": [{"description": "Trending detail request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.TrendingDetailRequest"}}], "path": "/google/trends/trending/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-videos": {"bodyParam": null, "bodyRequired": false, "id": "google-videos", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "1-based page number; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer", "x-example": 1}, {"description": "Results per page; defaults to 10, clamped to 1..50", "in": "query", "maximum": 50, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Two-letter country code; defaults to us", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Google UI language; defaults to en", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/google/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["google-finance-analyst-articles", "google-finance-chart", "google-finance-classification", "google-finance-company", "google-finance-context", "google-finance-financials", "google-finance-markets-category-news", "google-finance-markets-category-stocks", "google-finance-markets-earnings", "google-finance-markets-featured", "google-finance-markets-headline", "google-finance-markets-indices", "google-finance-markets-movers", "google-finance-markets-top", "google-finance-markets-trending", "google-finance-news", "google-finance-quote", "google-finance-related", "google-finance-search", "google-finance-ticker", "google-jobs", "google-map-place", "google-map-place-photos", "google-map-place-reviews", "google-map-search", "google-news", "google-news-search", "google-suggest", "google-trends-categories", "google-trends-enums", "google-trends-explore", "google-trends-explore-interest-by-region", "google-trends-explore-interest-over-time", "google-trends-explore-related-topics", "google-trends-explore-rising-queries", "google-trends-explore-top-queries", "google-trends-locations", "google-trends-trending", "google-trends-trending-detail", "google-videos"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-google-ruby/0.2.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('finance_analyst_articles') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-analyst-articles', params, response_type: response_type)
      end
      define_method('finance_chart') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-chart', params, response_type: response_type)
      end
      define_method('finance_classification') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-classification', params, response_type: response_type)
      end
      define_method('finance_company') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-company', params, response_type: response_type)
      end
      define_method('finance_context') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-context', params, response_type: response_type)
      end
      define_method('finance_financials') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-financials', params, response_type: response_type)
      end
      define_method('finance_markets_category_news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-category-news', params, response_type: response_type)
      end
      define_method('finance_markets_category_stocks') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-category-stocks', params, response_type: response_type)
      end
      define_method('finance_markets_earnings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-earnings', params, response_type: response_type)
      end
      define_method('finance_markets_featured') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-featured', params, response_type: response_type)
      end
      define_method('finance_markets_headline') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-headline', params, response_type: response_type)
      end
      define_method('finance_markets_indices') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-indices', params, response_type: response_type)
      end
      define_method('finance_markets_movers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-movers', params, response_type: response_type)
      end
      define_method('finance_markets_top') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-top', params, response_type: response_type)
      end
      define_method('finance_markets_trending') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-markets-trending', params, response_type: response_type)
      end
      define_method('finance_news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-news', params, response_type: response_type)
      end
      define_method('finance_quote') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-quote', params, response_type: response_type)
      end
      define_method('finance_related') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-related', params, response_type: response_type)
      end
      define_method('finance_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-search', params, response_type: response_type)
      end
      define_method('finance_ticker') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-finance-ticker', params, response_type: response_type)
      end
      define_method('jobs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-jobs', params, response_type: response_type)
      end
      define_method('map_place') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-map-place', params, response_type: response_type)
      end
      define_method('map_place_photos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-map-place-photos', params, response_type: response_type)
      end
      define_method('map_place_reviews') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-map-place-reviews', params, response_type: response_type)
      end
      define_method('map_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-map-search', params, response_type: response_type)
      end
      define_method('news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-news', params, response_type: response_type)
      end
      define_method('news_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-news-search', params, response_type: response_type)
      end
      define_method('suggest') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-suggest', params, response_type: response_type)
      end
      define_method('trends_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-categories', params, response_type: response_type)
      end
      define_method('trends_enums') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-enums', params, response_type: response_type)
      end
      define_method('trends_explore') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-explore', params, response_type: response_type)
      end
      define_method('trends_explore_interest_by_region') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-explore-interest-by-region', params, response_type: response_type)
      end
      define_method('trends_explore_interest_over_time') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-explore-interest-over-time', params, response_type: response_type)
      end
      define_method('trends_explore_related_topics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-explore-related-topics', params, response_type: response_type)
      end
      define_method('trends_explore_rising_queries') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-explore-rising-queries', params, response_type: response_type)
      end
      define_method('trends_explore_top_queries') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-explore-top-queries', params, response_type: response_type)
      end
      define_method('trends_locations') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-locations', params, response_type: response_type)
      end
      define_method('trends_trending') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-trending', params, response_type: response_type)
      end
      define_method('trends_trending_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-trends-trending-detail', params, response_type: response_type)
      end
      define_method('videos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('google-videos', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end

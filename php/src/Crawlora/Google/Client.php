<?php

declare(strict_types=1);

namespace Crawlora\Google;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'google';
    public const VERSION = '0.1.1';
    public const OPERATION_COUNT = 40;
    public const OPERATION_IDS = ["google-finance-analyst-articles", "google-finance-chart", "google-finance-classification", "google-finance-company", "google-finance-context", "google-finance-financials", "google-finance-markets-category-news", "google-finance-markets-category-stocks", "google-finance-markets-earnings", "google-finance-markets-featured", "google-finance-markets-headline", "google-finance-markets-indices", "google-finance-markets-movers", "google-finance-markets-top", "google-finance-markets-trending", "google-finance-news", "google-finance-quote", "google-finance-related", "google-finance-search", "google-finance-ticker", "google-jobs", "google-map-place", "google-map-place-photos", "google-map-place-reviews", "google-map-search", "google-news", "google-news-search", "google-suggest", "google-trends-categories", "google-trends-enums", "google-trends-explore", "google-trends-explore-interest-by-region", "google-trends-explore-interest-over-time", "google-trends-explore-related-topics", "google-trends-explore-rising-queries", "google-trends-explore-top-queries", "google-trends-locations", "google-trends-trending", "google-trends-trending-detail", "google-videos"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"google-finance-analyst-articles": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-analyst-articles", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/analyst-articles/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-chart": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-chart", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}, {"description": "Window: 1d, 5d, 1m, 6m, ytd, 1y, 5y, max", "in": "query", "name": "window", "type": "string"}], "path": "/google/finance/chart/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "window", "type": "string"}], "security": ["ApiKeyAuth"]}, "google-finance-classification": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-classification", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/classification/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-company": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-company", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/company/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-context": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-context", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "apple"}], "path": "/google/finance/context", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "google-finance-financials": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-financials", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/financials/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-category-news": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-category-news", "method": "GET", "params": [{"description": "Google Finance category id", "in": "path", "name": "category", "required": true, "type": "string", "x-example": "2"}, {"description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/google/finance/markets/categories/{category}/news", "pathParams": ["category"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-category-stocks": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-category-stocks", "method": "GET", "params": [{"description": "Google Finance category id", "in": "path", "name": "category", "required": true, "type": "string", "x-example": "2"}, {"description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/google/finance/markets/categories/{category}/stocks", "pathParams": ["category"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-earnings": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-earnings", "method": "GET", "params": [], "path": "/google/finance/markets/earnings", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-featured": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-featured", "method": "GET", "params": [], "path": "/google/finance/markets/featured", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-headline": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-headline", "method": "GET", "params": [], "path": "/google/finance/markets/headline", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-indices": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-indices", "method": "GET", "params": [], "path": "/google/finance/markets/indices", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-markets-movers": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-movers", "method": "GET", "params": [{"description": "Comma-separated numeric categories", "in": "query", "name": "categories", "type": "string"}, {"description": "Result count", "in": "query", "name": "count", "type": "integer"}, {"description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/google/finance/markets/movers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "categories", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-top": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-top", "method": "GET", "params": [{"description": "Google Finance metric id", "in": "query", "name": "metric", "type": "integer"}, {"description": "Page number", "in": "query", "name": "page", "type": "integer"}], "path": "/google/finance/markets/top", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "metric", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-markets-trending": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-markets-trending", "method": "GET", "params": [{"description": "Result limit", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/finance/markets/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-news": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-news", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}, {"description": "Article limit", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/finance/news/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-finance-quote": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-quote", "method": "GET", "params": [{"description": "Stock symbol to fetch the latest quote for (e.g., AAPL:NASDAQ, BTC-USD)", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/quote/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-related": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-related", "method": "GET", "params": [{"description": "Quote identifier such as AAPL:NASDAQ", "in": "path", "name": "quote", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}], "path": "/google/finance/related/{quote}", "pathParams": ["quote"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-finance-search": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-search", "method": "GET", "params": [{"description": "Keyword to search for (e.g., Apple)", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Apple"}], "path": "/google/finance/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "google-finance-ticker": {"bodyParam": null, "bodyRequired": false, "id": "google-finance-ticker", "method": "GET", "params": [{"description": "Ticker symbol to fetch data for example:AAPL:NASDAQ, BTC-USD ", "in": "path", "name": "ticker", "required": true, "type": "string", "x-example": "AAPL:NASDAQ"}, {"description": "Time window for the ticker data (default: 1d), options: 1d, 5d, 1m, 6m, 1y, 5y, max", "in": "query", "name": "window", "type": "string"}], "path": "/google/finance/ticker/{ticker}", "pathParams": ["ticker"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "window", "type": "string"}], "security": ["ApiKeyAuth"]}, "google-jobs": {"bodyParam": "option", "bodyRequired": true, "id": "google-jobs", "method": "POST", "params": [{"description": "Google Jobs search payload", "in": "body", "name": "option", "required": true, "schema": {"$ref": "#/definitions/google.JobsOption"}}], "path": "/google/jobs", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-map-place": {"bodyParam": null, "bodyRequired": false, "id": "google-map-place", "method": "GET", "params": [{"description": "Google Place ID", "in": "path", "name": "place_id", "required": true, "type": "string", "x-example": "ChIJs3cv0KuvEmsRHcXYwNJ6GU0"}], "path": "/google/map/place/{place_id}", "pathParams": ["place_id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-map-place-photos": {"bodyParam": null, "bodyRequired": false, "id": "google-map-place-photos", "method": "GET", "params": [{"description": "Google Place ID", "in": "path", "name": "place_id", "required": true, "type": "string", "x-example": "ChIJs3cv0KuvEmsRHcXYwNJ6GU0"}, {"description": "Maximum number of photos to return. Omit or 0 for all captured.", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/map/place/{place_id}/photos", "pathParams": ["place_id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-map-place-reviews": {"bodyParam": null, "bodyRequired": false, "id": "google-map-place-reviews", "method": "GET", "params": [{"description": "Google Place ID", "in": "path", "name": "place_id", "required": true, "type": "string", "x-example": "ChIJs3cv0KuvEmsRHcXYwNJ6GU0"}, {"description": "Maximum number of reviews to return. Omit or 0 for all captured.", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/map/place/{place_id}/reviews", "pathParams": ["place_id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-map-search": {"bodyParam": "mapSearchOption", "bodyRequired": true, "id": "google-map-search", "method": "POST", "params": [{"description": "Search options", "in": "body", "name": "mapSearchOption", "required": true, "schema": {"$ref": "#/definitions/google.MapSearchOption"}}], "path": "/google/map/search", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-news": {"bodyParam": null, "bodyRequired": false, "id": "google-news", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "1-based page within the current finite result snapshot; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer", "x-example": 1}, {"description": "Results per page; defaults to 10, clamped to 1..50", "in": "query", "maximum": 50, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Two-letter country code; defaults to us", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Google UI language; defaults to en", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/google/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "google-news-search": {"bodyParam": "searchOption", "bodyRequired": true, "id": "google-news-search", "method": "POST", "params": [{"description": "Search options; keyword, language and country are required. limit defaults to 10 and is clamped to 10..100; page defaults to 1.", "in": "body", "name": "searchOption", "required": true, "schema": {"$ref": "#/definitions/google.SearchOption"}}], "path": "/google/news", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-suggest": {"bodyParam": null, "bodyRequired": false, "id": "google-suggest", "method": "GET", "params": [{"description": "Search query prefix", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "Suggestions to return; defaults to 10, clamped to 1..12", "in": "query", "maximum": 12, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Google result country; defaults to us", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Google UI language; defaults to en", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": "web", "description": "Suggestion source; defaults to web", "enum": ["web", "youtube", "shopping"], "in": "query", "name": "source", "type": "string"}, {"description": "Add Google's type, relevance score, and description to each suggestion; defaults to false", "in": "query", "name": "rich", "type": "boolean", "x-example": false}], "path": "/google/suggest", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"enum": ["web", "youtube", "shopping"], "in": "query", "name": "source", "type": "string"}, {"in": "query", "name": "rich", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "google-trends-categories": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-categories", "method": "GET", "params": [], "path": "/google/trends/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-enums": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-enums", "method": "GET", "params": [], "path": "/google/trends/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-interest-by-region": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-interest-by-region", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/interest-by-region", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-interest-over-time": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-interest-over-time", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/interest-over-time", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-related-topics": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-related-topics", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/related-topics", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-rising-queries": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-rising-queries", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/rising-queries", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-explore-top-queries": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-explore-top-queries", "method": "POST", "params": [{"description": "Explore request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.ExploreRequest"}}], "path": "/google/trends/explore/top-queries", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-locations": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-locations", "method": "GET", "params": [], "path": "/google/trends/locations", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-trends-trending": {"bodyParam": null, "bodyRequired": false, "id": "google-trends-trending", "method": "GET", "params": [{"default": "US", "description": "Country/territory location code", "enum": ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "IO", "VG", "BN", "BG", "BF", "BI", "KH", "CM", "CA", "CV", "BQ", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "XK", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "KP", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "KR", "SS", "ES", "LK", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UM", "VI", "UG", "UA", "AE", "GB", "US", "UY", "UZ", "VU", "VA", "VE", "VN", "WF", "EH", "YE", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string"}, {"default": "en-US", "description": "Google Trends UI locale", "in": "query", "name": "hl", "type": "string"}, {"default": 0, "description": "Timezone offset minutes", "in": "query", "name": "tz", "type": "integer"}, {"default": "24h", "description": "Trend window", "enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "window", "type": "string"}, {"description": "Alias for window", "enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "time_range", "type": "string"}, {"default": 0, "description": "Trending category id", "enum": [0, 3, 47, 44, 22, 12, 5, 7, 71, 8, 45, 65, 11, 13, 958, 19, 16, 299, 14, 66, 29, 533, 174, 18, 20, 67], "in": "query", "name": "category", "type": "integer"}, {"default": "all", "description": "Trend status filter", "enum": ["all", "active", "ended"], "in": "query", "name": "status", "type": "string"}, {"default": "relevance", "description": "Sort mode", "enum": ["relevance", "title", "recency", "search_volume"], "in": "query", "name": "sort_by", "type": "string"}, {"default": 20, "description": "Maximum rows to return", "in": "query", "name": "limit", "type": "integer"}], "path": "/google/trends/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "IO", "VG", "BN", "BG", "BF", "BI", "KH", "CM", "CA", "CV", "BQ", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "XK", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "KP", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "KR", "SS", "ES", "LK", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UM", "VI", "UG", "UA", "AE", "GB", "US", "UY", "UZ", "VU", "VA", "VE", "VN", "WF", "EH", "YE", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string"}, {"in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "tz", "type": "integer"}, {"enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "window", "type": "string"}, {"enum": ["4h", "24h", "48h", "7d"], "in": "query", "name": "time_range", "type": "string"}, {"enum": ["0", "3", "47", "44", "22", "12", "5", "7", "71", "8", "45", "65", "11", "13", "958", "19", "16", "299", "14", "66", "29", "533", "174", "18", "20", "67"], "in": "query", "name": "category", "type": "integer"}, {"enum": ["all", "active", "ended"], "in": "query", "name": "status", "type": "string"}, {"enum": ["relevance", "title", "recency", "search_volume"], "in": "query", "name": "sort_by", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "google-trends-trending-detail": {"bodyParam": "request", "bodyRequired": true, "id": "google-trends-trending-detail", "method": "POST", "params": [{"description": "Trending detail request", "in": "body", "name": "request", "required": true, "schema": {"$ref": "#/definitions/trends.TrendingDetailRequest"}}], "path": "/google/trends/trending/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "google-videos": {"bodyParam": null, "bodyRequired": false, "id": "google-videos", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "1-based page number; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer", "x-example": 1}, {"description": "Results per page; defaults to 10, clamped to 1..50", "in": "query", "maximum": 50, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Two-letter country code; defaults to us", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Google UI language; defaults to en", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/google/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-google-php/0.1.1',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function finance_analyst_articles(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-analyst-articles", $params, $responseType);
    }
    public function finance_chart(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-chart", $params, $responseType);
    }
    public function finance_classification(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-classification", $params, $responseType);
    }
    public function finance_company(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-company", $params, $responseType);
    }
    public function finance_context(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-context", $params, $responseType);
    }
    public function finance_financials(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-financials", $params, $responseType);
    }
    public function finance_markets_category_news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-category-news", $params, $responseType);
    }
    public function finance_markets_category_stocks(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-category-stocks", $params, $responseType);
    }
    public function finance_markets_earnings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-earnings", $params, $responseType);
    }
    public function finance_markets_featured(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-featured", $params, $responseType);
    }
    public function finance_markets_headline(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-headline", $params, $responseType);
    }
    public function finance_markets_indices(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-indices", $params, $responseType);
    }
    public function finance_markets_movers(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-movers", $params, $responseType);
    }
    public function finance_markets_top(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-top", $params, $responseType);
    }
    public function finance_markets_trending(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-markets-trending", $params, $responseType);
    }
    public function finance_news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-news", $params, $responseType);
    }
    public function finance_quote(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-quote", $params, $responseType);
    }
    public function finance_related(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-related", $params, $responseType);
    }
    public function finance_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-search", $params, $responseType);
    }
    public function finance_ticker(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-finance-ticker", $params, $responseType);
    }
    public function jobs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-jobs", $params, $responseType);
    }
    public function map_place(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-map-place", $params, $responseType);
    }
    public function map_place_photos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-map-place-photos", $params, $responseType);
    }
    public function map_place_reviews(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-map-place-reviews", $params, $responseType);
    }
    public function map_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-map-search", $params, $responseType);
    }
    public function news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-news", $params, $responseType);
    }
    public function news_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-news-search", $params, $responseType);
    }
    public function suggest(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-suggest", $params, $responseType);
    }
    public function trends_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-categories", $params, $responseType);
    }
    public function trends_enums(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-enums", $params, $responseType);
    }
    public function trends_explore(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-explore", $params, $responseType);
    }
    public function trends_explore_interest_by_region(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-explore-interest-by-region", $params, $responseType);
    }
    public function trends_explore_interest_over_time(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-explore-interest-over-time", $params, $responseType);
    }
    public function trends_explore_related_topics(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-explore-related-topics", $params, $responseType);
    }
    public function trends_explore_rising_queries(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-explore-rising-queries", $params, $responseType);
    }
    public function trends_explore_top_queries(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-explore-top-queries", $params, $responseType);
    }
    public function trends_locations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-locations", $params, $responseType);
    }
    public function trends_trending(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-trending", $params, $responseType);
    }
    public function trends_trending_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-trends-trending-detail", $params, $responseType);
    }
    public function videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("google-videos", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}

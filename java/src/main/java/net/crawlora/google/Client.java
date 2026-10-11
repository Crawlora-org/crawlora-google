package net.crawlora.google;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Google endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 40;
    public static final List<String> OPERATION_IDS = List.of(
            "google-finance-analyst-articles",
            "google-finance-chart",
            "google-finance-classification",
            "google-finance-company",
            "google-finance-context",
            "google-finance-financials",
            "google-finance-markets-category-news",
            "google-finance-markets-category-stocks",
            "google-finance-markets-earnings",
            "google-finance-markets-featured",
            "google-finance-markets-headline",
            "google-finance-markets-indices",
            "google-finance-markets-movers",
            "google-finance-markets-top",
            "google-finance-markets-trending",
            "google-finance-news",
            "google-finance-quote",
            "google-finance-related",
            "google-finance-search",
            "google-finance-ticker",
            "google-jobs",
            "google-map-place",
            "google-map-place-photos",
            "google-map-place-reviews",
            "google-map-search",
            "google-news",
            "google-news-search",
            "google-suggest",
            "google-trends-categories",
            "google-trends-enums",
            "google-trends-explore",
            "google-trends-explore-interest-by-region",
            "google-trends-explore-interest-over-time",
            "google-trends-explore-related-topics",
            "google-trends-explore-rising-queries",
            "google-trends-explore-top-queries",
            "google-trends-locations",
            "google-trends-trending",
            "google-trends-trending-detail",
            "google-videos"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("google-finance-analyst-articles", new Operation("google-finance-analyst-articles", "GET", "/google/finance/analyst-articles/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-chart", new Operation("google-finance-chart", "GET", "/google/finance/chart/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv")), Map.entry("window", new Param("window", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-classification", new Operation("google-finance-classification", "GET", "/google/finance/classification/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-company", new Operation("google-finance-company", "GET", "/google/finance/company/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-context", new Operation("google-finance-context", "GET", "/google/finance/context", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-financials", new Operation("google-finance-financials", "GET", "/google/finance/financials/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-markets-category-news", new Operation("google-finance-markets-category-news", "GET", "/google/finance/markets/categories/{category}/news", Map.ofEntries(Map.entry("category", new Param("category", "path", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-markets-category-stocks", new Operation("google-finance-markets-category-stocks", "GET", "/google/finance/markets/categories/{category}/stocks", Map.ofEntries(Map.entry("category", new Param("category", "path", true, "string", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-markets-earnings", new Operation("google-finance-markets-earnings", "GET", "/google/finance/markets/earnings", Map.of(), List.of("application/json")));
        operations.put("google-finance-markets-featured", new Operation("google-finance-markets-featured", "GET", "/google/finance/markets/featured", Map.of(), List.of("application/json")));
        operations.put("google-finance-markets-headline", new Operation("google-finance-markets-headline", "GET", "/google/finance/markets/headline", Map.of(), List.of("application/json")));
        operations.put("google-finance-markets-indices", new Operation("google-finance-markets-indices", "GET", "/google/finance/markets/indices", Map.of(), List.of("application/json")));
        operations.put("google-finance-markets-movers", new Operation("google-finance-markets-movers", "GET", "/google/finance/markets/movers", Map.ofEntries(Map.entry("categories", new Param("categories", "query", false, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-markets-top", new Operation("google-finance-markets-top", "GET", "/google/finance/markets/top", Map.ofEntries(Map.entry("metric", new Param("metric", "query", false, "integer", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-markets-trending", new Operation("google-finance-markets-trending", "GET", "/google/finance/markets/trending", Map.ofEntries(Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-news", new Operation("google-finance-news", "GET", "/google/finance/news/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-quote", new Operation("google-finance-quote", "GET", "/google/finance/quote/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-related", new Operation("google-finance-related", "GET", "/google/finance/related/{quote}", Map.ofEntries(Map.entry("quote", new Param("quote", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-search", new Operation("google-finance-search", "GET", "/google/finance/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-finance-ticker", new Operation("google-finance-ticker", "GET", "/google/finance/ticker/{ticker}", Map.ofEntries(Map.entry("ticker", new Param("ticker", "path", true, "string", List.of(), "csv")), Map.entry("window", new Param("window", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-jobs", new Operation("google-jobs", "POST", "/google/jobs", Map.of(), List.of("application/json"), "option"));
        operations.put("google-map-place", new Operation("google-map-place", "GET", "/google/map/place/{place_id}", Map.ofEntries(Map.entry("place_id", new Param("place_id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-map-place-photos", new Operation("google-map-place-photos", "GET", "/google/map/place/{place_id}/photos", Map.ofEntries(Map.entry("place_id", new Param("place_id", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-map-place-reviews", new Operation("google-map-place-reviews", "GET", "/google/map/place/{place_id}/reviews", Map.ofEntries(Map.entry("place_id", new Param("place_id", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-map-search", new Operation("google-map-search", "POST", "/google/map/search", Map.of(), List.of("application/json"), "mapSearchOption"));
        operations.put("google-news", new Operation("google-news", "GET", "/google/news", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-news-search", new Operation("google-news-search", "POST", "/google/news", Map.of(), List.of("application/json"), "searchOption"));
        operations.put("google-suggest", new Operation("google-suggest", "GET", "/google/suggest", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv")), Map.entry("source", new Param("source", "query", false, "string", List.of("web", "youtube", "shopping"), "csv")), Map.entry("rich", new Param("rich", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-trends-categories", new Operation("google-trends-categories", "GET", "/google/trends/categories", Map.of(), List.of("application/json")));
        operations.put("google-trends-enums", new Operation("google-trends-enums", "GET", "/google/trends/enums", Map.of(), List.of("application/json")));
        operations.put("google-trends-explore", new Operation("google-trends-explore", "POST", "/google/trends/explore", Map.of(), List.of("application/json"), "request"));
        operations.put("google-trends-explore-interest-by-region", new Operation("google-trends-explore-interest-by-region", "POST", "/google/trends/explore/interest-by-region", Map.of(), List.of("application/json"), "request"));
        operations.put("google-trends-explore-interest-over-time", new Operation("google-trends-explore-interest-over-time", "POST", "/google/trends/explore/interest-over-time", Map.of(), List.of("application/json"), "request"));
        operations.put("google-trends-explore-related-topics", new Operation("google-trends-explore-related-topics", "POST", "/google/trends/explore/related-topics", Map.of(), List.of("application/json"), "request"));
        operations.put("google-trends-explore-rising-queries", new Operation("google-trends-explore-rising-queries", "POST", "/google/trends/explore/rising-queries", Map.of(), List.of("application/json"), "request"));
        operations.put("google-trends-explore-top-queries", new Operation("google-trends-explore-top-queries", "POST", "/google/trends/explore/top-queries", Map.of(), List.of("application/json"), "request"));
        operations.put("google-trends-locations", new Operation("google-trends-locations", "GET", "/google/trends/locations", Map.of(), List.of("application/json")));
        operations.put("google-trends-trending", new Operation("google-trends-trending", "GET", "/google/trends/trending", Map.ofEntries(Map.entry("geo", new Param("geo", "query", false, "string", List.of("AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "IO", "VG", "BN", "BG", "BF", "BI", "KH", "CM", "CA", "CV", "BQ", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "XK", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "KP", "MK", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "KR", "SS", "ES", "LK", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UM", "VI", "UG", "UA", "AE", "GB", "US", "UY", "UZ", "VU", "VA", "VE", "VN", "WF", "EH", "YE", "ZM", "ZW"), "csv")), Map.entry("hl", new Param("hl", "query", false, "string", List.of(), "csv")), Map.entry("tz", new Param("tz", "query", false, "integer", List.of(), "csv")), Map.entry("window", new Param("window", "query", false, "string", List.of("4h", "24h", "48h", "7d"), "csv")), Map.entry("time_range", new Param("time_range", "query", false, "string", List.of("4h", "24h", "48h", "7d"), "csv")), Map.entry("category", new Param("category", "query", false, "integer", List.of("0", "3", "47", "44", "22", "12", "5", "7", "71", "8", "45", "65", "11", "13", "958", "19", "16", "299", "14", "66", "29", "533", "174", "18", "20", "67"), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of("all", "active", "ended"), "csv")), Map.entry("sort_by", new Param("sort_by", "query", false, "string", List.of("relevance", "title", "recency", "search_volume"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("google-trends-trending-detail", new Operation("google-trends-trending-detail", "POST", "/google/trends/trending/detail", Map.of(), List.of("application/json"), "request"));
        operations.put("google-videos", new Operation("google-videos", "GET", "/google/videos", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Google operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object financeAnalystArticles(Map<String, ?> params) { return request("google-finance-analyst-articles", params); }
    public Object financeChart(Map<String, ?> params) { return request("google-finance-chart", params); }
    public Object financeClassification(Map<String, ?> params) { return request("google-finance-classification", params); }
    public Object financeCompany(Map<String, ?> params) { return request("google-finance-company", params); }
    public Object financeContext(Map<String, ?> params) { return request("google-finance-context", params); }
    public Object financeFinancials(Map<String, ?> params) { return request("google-finance-financials", params); }
    public Object financeMarketsCategoryNews(Map<String, ?> params) { return request("google-finance-markets-category-news", params); }
    public Object financeMarketsCategoryStocks(Map<String, ?> params) { return request("google-finance-markets-category-stocks", params); }
    public Object financeMarketsEarnings(Map<String, ?> params) { return request("google-finance-markets-earnings", params); }
    public Object financeMarketsFeatured(Map<String, ?> params) { return request("google-finance-markets-featured", params); }
    public Object financeMarketsHeadline(Map<String, ?> params) { return request("google-finance-markets-headline", params); }
    public Object financeMarketsIndices(Map<String, ?> params) { return request("google-finance-markets-indices", params); }
    public Object financeMarketsMovers(Map<String, ?> params) { return request("google-finance-markets-movers", params); }
    public Object financeMarketsTop(Map<String, ?> params) { return request("google-finance-markets-top", params); }
    public Object financeMarketsTrending(Map<String, ?> params) { return request("google-finance-markets-trending", params); }
    public Object financeNews(Map<String, ?> params) { return request("google-finance-news", params); }
    public Object financeQuote(Map<String, ?> params) { return request("google-finance-quote", params); }
    public Object financeRelated(Map<String, ?> params) { return request("google-finance-related", params); }
    public Object financeSearch(Map<String, ?> params) { return request("google-finance-search", params); }
    public Object financeTicker(Map<String, ?> params) { return request("google-finance-ticker", params); }
    public Object jobs(Map<String, ?> params) { return request("google-jobs", params); }
    public Object mapPlace(Map<String, ?> params) { return request("google-map-place", params); }
    public Object mapPlacePhotos(Map<String, ?> params) { return request("google-map-place-photos", params); }
    public Object mapPlaceReviews(Map<String, ?> params) { return request("google-map-place-reviews", params); }
    public Object mapSearch(Map<String, ?> params) { return request("google-map-search", params); }
    public Object news(Map<String, ?> params) { return request("google-news", params); }
    public Object newsSearch(Map<String, ?> params) { return request("google-news-search", params); }
    public Object suggest(Map<String, ?> params) { return request("google-suggest", params); }
    public Object trendsCategories(Map<String, ?> params) { return request("google-trends-categories", params); }
    public Object trendsEnums(Map<String, ?> params) { return request("google-trends-enums", params); }
    public Object trendsExplore(Map<String, ?> params) { return request("google-trends-explore", params); }
    public Object trendsExploreInterestByRegion(Map<String, ?> params) { return request("google-trends-explore-interest-by-region", params); }
    public Object trendsExploreInterestOverTime(Map<String, ?> params) { return request("google-trends-explore-interest-over-time", params); }
    public Object trendsExploreRelatedTopics(Map<String, ?> params) { return request("google-trends-explore-related-topics", params); }
    public Object trendsExploreRisingQueries(Map<String, ?> params) { return request("google-trends-explore-rising-queries", params); }
    public Object trendsExploreTopQueries(Map<String, ?> params) { return request("google-trends-explore-top-queries", params); }
    public Object trendsLocations(Map<String, ?> params) { return request("google-trends-locations", params); }
    public Object trendsTrending(Map<String, ?> params) { return request("google-trends-trending", params); }
    public Object trendsTrendingDetail(Map<String, ?> params) { return request("google-trends-trending-detail", params); }
    public Object videos(Map<String, ?> params) { return request("google-videos", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}

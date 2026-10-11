# Crawlora Google API client for Java

The official Java client for Crawlora's hosted Google API. It exposes 40 endpoints covering Maps search, places, reviews and photos; News; Trends; Finance quotes and markets; suggestions; videos; and jobs. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-google</artifactId>
  <version>0.1.1</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-java-console) to get an API key.

```java
import net.crawlora.google.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.news(Map.ofEntries(Map.entry("q", "artificial intelligence")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Google API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-google/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/google/finance/analyst-articles/{quote}` | `google-finance-analyst-articles` | Google Finance analyst articles |
| `GET` | `/google/finance/chart/{quote}` | `google-finance-chart` | Google Finance chart data |
| `GET` | `/google/finance/classification/{quote}` | `google-finance-classification` | Google Finance classification data |
| `GET` | `/google/finance/company/{quote}` | `google-finance-company` | Google Finance company data |
| `GET` | `/google/finance/context` | `google-finance-context` | Find Google Finance instruments by query |
| `GET` | `/google/finance/financials/{quote}` | `google-finance-financials` | Google Finance financial statements |
| `GET` | `/google/finance/markets/categories/{category}/news` | `google-finance-markets-category-news` | Google Finance category news |
| `GET` | `/google/finance/markets/categories/{category}/stocks` | `google-finance-markets-category-stocks` | Google Finance category stocks |
| `GET` | `/google/finance/markets/earnings` | `google-finance-markets-earnings` | Google Finance earnings calendar |
| `GET` | `/google/finance/markets/featured` | `google-finance-markets-featured` | Google Finance featured stocks |
| `GET` | `/google/finance/markets/headline` | `google-finance-markets-headline` | Google Finance top headline |
| `GET` | `/google/finance/markets/indices` | `google-finance-markets-indices` | Google Finance market indices |
| `GET` | `/google/finance/markets/movers` | `google-finance-markets-movers` | Google Finance market movers |
| `GET` | `/google/finance/markets/top` | `google-finance-markets-top` | Google Finance top stocks by metric |
| `GET` | `/google/finance/markets/trending` | `google-finance-markets-trending` | Google Finance trending stocks |
| `GET` | `/google/finance/news/{quote}` | `google-finance-news` | Google Finance quote news |
| `GET` | `/google/finance/quote/{quote}` | `google-finance-quote` | Google Finance Quote API |
| `GET` | `/google/finance/related/{quote}` | `google-finance-related` | Google Finance related instruments |
| `GET` | `/google/finance/search` | `google-finance-search` | Google Finance Search API |
| `GET` | `/google/finance/ticker/{ticker}` | `google-finance-ticker` | Google Finance Ticker API |
| `POST` | `/google/jobs` | `google-jobs` | Search Google Jobs |
| `GET` | `/google/map/place/{place_id}` | `google-map-place` | Google Maps place details API |
| `GET` | `/google/map/place/{place_id}/photos` | `google-map-place-photos` | Google Maps place photos API |
| `GET` | `/google/map/place/{place_id}/reviews` | `google-map-place-reviews` | Google Maps place reviews API |
| `POST` | `/google/map/search` | `google-map-search` | Google Maps search API |
| `GET` | `/google/news` | `google-news` | Search Google News |
| `POST` | `/google/news` | `google-news-search` | Search Google News with JSON |
| `GET` | `/google/suggest` | `google-suggest` | Suggest Google search queries |
| `GET` | `/google/trends/categories` | `google-trends-categories` | Google Trends categories |
| `GET` | `/google/trends/enums` | `google-trends-enums` | Google Trends enum metadata |
| `POST` | `/google/trends/explore` | `google-trends-explore` | Google Trends explore data |
| `POST` | `/google/trends/explore/interest-by-region` | `google-trends-explore-interest-by-region` | Google Trends interest by region |
| `POST` | `/google/trends/explore/interest-over-time` | `google-trends-explore-interest-over-time` | Google Trends interest over time |
| `POST` | `/google/trends/explore/related-topics` | `google-trends-explore-related-topics` | Google Trends related topics |
| `POST` | `/google/trends/explore/rising-queries` | `google-trends-explore-rising-queries` | Google Trends explore rising queries |
| `POST` | `/google/trends/explore/top-queries` | `google-trends-explore-top-queries` | Google Trends explore top queries |
| `GET` | `/google/trends/locations` | `google-trends-locations` | Google Trends locations |
| `GET` | `/google/trends/trending` | `google-trends-trending` | Google Trends trending now data |
| `POST` | `/google/trends/trending/detail` | `google-trends-trending-detail` | Google Trends trending term detail |
| `GET` | `/google/videos` | `google-videos` | Search Google video results |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-google)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-java-api-docs)

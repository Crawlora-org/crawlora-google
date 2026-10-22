# Google API endpoint reference and client usage

This reference lists all 40 public Google API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/google`, `crawlora-google`, and `crawlora-google` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Google locally; Crawlora is independent from and not endorsed by Google or its owners.

The package tracks the public API contract revision `sha256:8db88e8b908a130295c5df80bead8c65485e1eb4a293ceaa55add4ec77d7d071` bundled with release `0.2.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `google`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `financeAnalystArticles` | `finance_analyst_articles` | `google.finance_analyst_articles` | `GET /google/finance/analyst-articles/{quote}` | `quote` (path, required) | Google Finance analyst articles |
| `financeChart` | `finance_chart` | `google.finance_chart` | `GET /google/finance/chart/{quote}` | `quote` (path, required), `window` (query, optional) | Google Finance chart data |
| `financeClassification` | `finance_classification` | `google.finance_classification` | `GET /google/finance/classification/{quote}` | `quote` (path, required) | Google Finance classification data |
| `financeCompany` | `finance_company` | `google.finance_company` | `GET /google/finance/company/{quote}` | `quote` (path, required) | Google Finance company data |
| `financeContext` | `finance_context` | `google.finance_context` | `GET /google/finance/context` | `q` (query, required) | Find Google Finance instruments by query |
| `financeFinancials` | `finance_financials` | `google.finance_financials` | `GET /google/finance/financials/{quote}` | `quote` (path, required) | Google Finance financial statements |
| `financeMarketsCategoryNews` | `finance_markets_category_news` | `google.finance_markets_category_news` | `GET /google/finance/markets/categories/{category}/news` | `category` (path, required), `offset` (query, optional) | Google Finance category news |
| `financeMarketsCategoryStocks` | `finance_markets_category_stocks` | `google.finance_markets_category_stocks` | `GET /google/finance/markets/categories/{category}/stocks` | `category` (path, required), `offset` (query, optional) | Google Finance category stocks |
| `financeMarketsEarnings` | `finance_markets_earnings` | `google.finance_markets_earnings` | `GET /google/finance/markets/earnings` | — | Google Finance earnings calendar |
| `financeMarketsFeatured` | `finance_markets_featured` | `google.finance_markets_featured` | `GET /google/finance/markets/featured` | — | Google Finance featured stocks |
| `financeMarketsHeadline` | `finance_markets_headline` | `google.finance_markets_headline` | `GET /google/finance/markets/headline` | — | Google Finance top headline |
| `financeMarketsIndices` | `finance_markets_indices` | `google.finance_markets_indices` | `GET /google/finance/markets/indices` | — | Google Finance market indices |
| `financeMarketsMovers` | `finance_markets_movers` | `google.finance_markets_movers` | `GET /google/finance/markets/movers` | `categories` (query, optional), `count` (query, optional), `offset` (query, optional) | Google Finance market movers |
| `financeMarketsTop` | `finance_markets_top` | `google.finance_markets_top` | `GET /google/finance/markets/top` | `metric` (query, optional), `page` (query, optional) | Google Finance top stocks by metric |
| `financeMarketsTrending` | `finance_markets_trending` | `google.finance_markets_trending` | `GET /google/finance/markets/trending` | `limit` (query, optional) | Google Finance trending stocks |
| `financeNews` | `finance_news` | `google.finance_news` | `GET /google/finance/news/{quote}` | `quote` (path, required), `limit` (query, optional) | Google Finance quote news |
| `financeQuote` | `finance_quote` | `google.finance_quote` | `GET /google/finance/quote/{quote}` | `quote` (path, required) | Google Finance Quote API |
| `financeRelated` | `finance_related` | `google.finance_related` | `GET /google/finance/related/{quote}` | `quote` (path, required) | Google Finance related instruments |
| `financeSearch` | `finance_search` | `google.finance_search` | `GET /google/finance/search` | `q` (query, required) | Google Finance Search API |
| `financeTicker` | `finance_ticker` | `google.finance_ticker` | `GET /google/finance/ticker/{ticker}` | `ticker` (path, required), `window` (query, optional) | Google Finance Ticker API |
| `jobs` | `jobs` | `google.jobs` | `POST /google/jobs` | `option` (body, required) | Search Google Jobs |
| `mapPlace` | `map_place` | `google.map_place` | `GET /google/map/place/{place_id}` | `place_id` (path, required) | Google Maps place details API |
| `mapPlacePhotos` | `map_place_photos` | `google.map_place_photos` | `GET /google/map/place/{place_id}/photos` | `place_id` (path, required), `limit` (query, optional) | Google Maps place photos API |
| `mapPlaceReviews` | `map_place_reviews` | `google.map_place_reviews` | `GET /google/map/place/{place_id}/reviews` | `place_id` (path, required), `limit` (query, optional) | Google Maps place reviews API |
| `mapSearch` | `map_search` | `google.map_search` | `POST /google/map/search` | `mapSearchOption` (body, required) | Google Maps search API |
| `news` | `news` | `google.news` | `GET /google/news` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Google News |
| `newsSearch` | `news_search` | `google.news_search` | `POST /google/news` | `searchOption` (body, required) | Search Google News with JSON |
| `suggest` | `suggest` | `google.suggest` | `GET /google/suggest` | `q` (query, required), `count` (query, optional), `country` (query, optional), `lang` (query, optional), `source` (query, optional; values: `web`, `youtube`, `shopping`), `rich` (query, optional) | Suggest Google search queries |
| `trendsCategories` | `trends_categories` | `google.trends_categories` | `GET /google/trends/categories` | — | Google Trends categories |
| `trendsEnums` | `trends_enums` | `google.trends_enums` | `GET /google/trends/enums` | — | Google Trends enum metadata |
| `trendsExplore` | `trends_explore` | `google.trends_explore` | `POST /google/trends/explore` | `request` (body, required) | Google Trends explore data |
| `trendsExploreInterestByRegion` | `trends_explore_interest_by_region` | `google.trends_explore_interest_by_region` | `POST /google/trends/explore/interest-by-region` | `request` (body, required) | Google Trends interest by region |
| `trendsExploreInterestOverTime` | `trends_explore_interest_over_time` | `google.trends_explore_interest_over_time` | `POST /google/trends/explore/interest-over-time` | `request` (body, required) | Google Trends interest over time |
| `trendsExploreRelatedTopics` | `trends_explore_related_topics` | `google.trends_explore_related_topics` | `POST /google/trends/explore/related-topics` | `request` (body, required) | Google Trends related topics |
| `trendsExploreRisingQueries` | `trends_explore_rising_queries` | `google.trends_explore_rising_queries` | `POST /google/trends/explore/rising-queries` | `request` (body, required) | Google Trends explore rising queries |
| `trendsExploreTopQueries` | `trends_explore_top_queries` | `google.trends_explore_top_queries` | `POST /google/trends/explore/top-queries` | `request` (body, required) | Google Trends explore top queries |
| `trendsLocations` | `trends_locations` | `google.trends_locations` | `GET /google/trends/locations` | — | Google Trends locations |
| `trendsTrending` | `trends_trending` | `google.trends_trending` | `GET /google/trends/trending` | `geo` (query, optional; values: `AF`, `AX`, `AL`, `DZ`, `AS`, `AD`, `AO`, `AI`, `AQ`, `AG`, `AR`, `AM`, `AW`, `AU`, `AT`, `AZ`, `BS`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BV`, `BR`, `IO`, `VG`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `BQ`, `KY`, `CF`, `TD`, `CL`, `CN`, `CX`, `CC`, `CO`, `KM`, `CG`, `CD`, `CK`, `CR`, `CI`, `HR`, `CU`, `CW`, `CY`, `CZ`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `SZ`, `ET`, `FK`, `FO`, `FJ`, `FI`, `FR`, `GF`, `PF`, `TF`, `GA`, `GM`, `GE`, `DE`, `GH`, `GI`, `GR`, `GL`, `GD`, `GP`, `GU`, `GT`, `GG`, `GN`, `GW`, `GY`, `HT`, `HM`, `HN`, `HK`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IM`, `IL`, `IT`, `JM`, `JP`, `JE`, `JO`, `KZ`, `KE`, `KI`, `XK`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MG`, `MW`, `MY`, `MV`, `ML`, `MT`, `MH`, `MQ`, `MR`, `MU`, `YT`, `MX`, `FM`, `MD`, `MC`, `MN`, `ME`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `NC`, `NZ`, `NI`, `NE`, `NG`, `NU`, `NF`, `KP`, `MK`, `MP`, `NO`, `OM`, `PK`, `PW`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PN`, `PL`, `PT`, `PR`, `QA`, `RE`, `RO`, `RU`, `RW`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SG`, `SX`, `SK`, `SI`, `SB`, `SO`, `ZA`, `GS`, `KR`, `SS`, `ES`, `LK`, `BL`, `SH`, `KN`, `LC`, `MF`, `PM`, `VC`, `SD`, `SR`, `SJ`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `TL`, `TG`, `TK`, `TO`, `TT`, `TN`, `TR`, `TM`, `TC`, `TV`, `UM`, `VI`, `UG`, `UA`, `AE`, `GB`, `US`, `UY`, `UZ`, `VU`, `VA`, `VE`, `VN`, `WF`, `EH`, `YE`, `ZM`, `ZW`), `hl` (query, optional), `tz` (query, optional), `window` (query, optional; values: `4h`, `24h`, `48h`, `7d`), `time_range` (query, optional; values: `4h`, `24h`, `48h`, `7d`), `category` (query, optional; values: `0`, `3`, `47`, `44`, `22`, `12`, `5`, `7`, `71`, `8`, `45`, `65`, `11`, `13`, `958`, `19`, `16`, `299`, `14`, `66`, `29`, `533`, `174`, `18`, `20`, `67`), `status` (query, optional; values: `all`, `active`, `ended`), `sort_by` (query, optional; values: `relevance`, `title`, `recency`, `search_volume`), `limit` (query, optional) | Google Trends trending now data |
| `trendsTrendingDetail` | `trends_trending_detail` | `google.trends_trending_detail` | `POST /google/trends/trending/detail` | `request` (body, required) | Google Trends trending term detail |
| `videos` | `videos` | `google.videos` | `GET /google/videos` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Google video results |

## Client forms

- JavaScript: import `GoogleClient` (also exported as `Client`) from `@crawlora-org/google`; use `new GoogleClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `GoogleClient` (also exported as `Client`) from `crawlora_google`; use `with GoogleClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncGoogleClient`, used with `async with` and `await`.
- Rust: add `crawlora-google` with Cargo; import `Client` and the generated operation parameter struct, then call `client.google.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-google/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.

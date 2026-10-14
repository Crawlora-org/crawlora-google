import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class GoogleClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-google-js/0.2.0" });
    this["financeAnalystArticles"] = (...args) => this.request("google-finance-analyst-articles", ...args);
    this["financeChart"] = (...args) => this.request("google-finance-chart", ...args);
    this["financeClassification"] = (...args) => this.request("google-finance-classification", ...args);
    this["financeCompany"] = (...args) => this.request("google-finance-company", ...args);
    this["financeContext"] = (...args) => this.request("google-finance-context", ...args);
    this["financeFinancials"] = (...args) => this.request("google-finance-financials", ...args);
    this["financeMarketsCategoryNews"] = (...args) => this.request("google-finance-markets-category-news", ...args);
    this["financeMarketsCategoryStocks"] = (...args) => this.request("google-finance-markets-category-stocks", ...args);
    this["financeMarketsEarnings"] = (...args) => this.request("google-finance-markets-earnings", ...args);
    this["financeMarketsFeatured"] = (...args) => this.request("google-finance-markets-featured", ...args);
    this["financeMarketsHeadline"] = (...args) => this.request("google-finance-markets-headline", ...args);
    this["financeMarketsIndices"] = (...args) => this.request("google-finance-markets-indices", ...args);
    this["financeMarketsMovers"] = (...args) => this.request("google-finance-markets-movers", ...args);
    this["financeMarketsTop"] = (...args) => this.request("google-finance-markets-top", ...args);
    this["financeMarketsTrending"] = (...args) => this.request("google-finance-markets-trending", ...args);
    this["financeNews"] = (...args) => this.request("google-finance-news", ...args);
    this["financeQuote"] = (...args) => this.request("google-finance-quote", ...args);
    this["financeRelated"] = (...args) => this.request("google-finance-related", ...args);
    this["financeSearch"] = (...args) => this.request("google-finance-search", ...args);
    this["financeTicker"] = (...args) => this.request("google-finance-ticker", ...args);
    this["jobs"] = (...args) => this.request("google-jobs", ...args);
    this["mapPlace"] = (...args) => this.request("google-map-place", ...args);
    this["mapPlacePhotos"] = (...args) => this.request("google-map-place-photos", ...args);
    this["mapPlaceReviews"] = (...args) => this.request("google-map-place-reviews", ...args);
    this["mapSearch"] = (...args) => this.request("google-map-search", ...args);
    this["news"] = (...args) => this.request("google-news", ...args);
    this["newsSearch"] = (...args) => this.request("google-news-search", ...args);
    this["suggest"] = (...args) => this.request("google-suggest", ...args);
    this["trendsCategories"] = (...args) => this.request("google-trends-categories", ...args);
    this["trendsEnums"] = (...args) => this.request("google-trends-enums", ...args);
    this["trendsExplore"] = (...args) => this.request("google-trends-explore", ...args);
    this["trendsExploreInterestByRegion"] = (...args) => this.request("google-trends-explore-interest-by-region", ...args);
    this["trendsExploreInterestOverTime"] = (...args) => this.request("google-trends-explore-interest-over-time", ...args);
    this["trendsExploreRelatedTopics"] = (...args) => this.request("google-trends-explore-related-topics", ...args);
    this["trendsExploreRisingQueries"] = (...args) => this.request("google-trends-explore-rising-queries", ...args);
    this["trendsExploreTopQueries"] = (...args) => this.request("google-trends-explore-top-queries", ...args);
    this["trendsLocations"] = (...args) => this.request("google-trends-locations", ...args);
    this["trendsTrending"] = (...args) => this.request("google-trends-trending", ...args);
    this["trendsTrendingDetail"] = (...args) => this.request("google-trends-trending-detail", ...args);
    this["videos"] = (...args) => this.request("google-videos", ...args);
  }
}

export { GoogleClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.2.0";
export default GoogleClient;

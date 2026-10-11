import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class GoogleClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeAnalystArticles(params: OperationParamsMap["google-finance-analyst-articles"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeChart(params: OperationParamsMap["google-finance-chart"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeClassification(params: OperationParamsMap["google-finance-classification"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeCompany(params: OperationParamsMap["google-finance-company"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeContext(params: OperationParamsMap["google-finance-context"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeFinancials(params: OperationParamsMap["google-finance-financials"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsCategoryNews(params: OperationParamsMap["google-finance-markets-category-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsCategoryStocks(params: OperationParamsMap["google-finance-markets-category-stocks"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsEarnings(params?: OperationParamsMap["google-finance-markets-earnings"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsFeatured(params?: OperationParamsMap["google-finance-markets-featured"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsHeadline(params?: OperationParamsMap["google-finance-markets-headline"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsIndices(params?: OperationParamsMap["google-finance-markets-indices"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsMovers(params?: OperationParamsMap["google-finance-markets-movers"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsTop(params?: OperationParamsMap["google-finance-markets-top"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeMarketsTrending(params?: OperationParamsMap["google-finance-markets-trending"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeNews(params: OperationParamsMap["google-finance-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeQuote(params: OperationParamsMap["google-finance-quote"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeRelated(params: OperationParamsMap["google-finance-related"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeSearch(params: OperationParamsMap["google-finance-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  financeTicker(params: OperationParamsMap["google-finance-ticker"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  jobs(params: OperationParamsMap["google-jobs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mapPlace(params: OperationParamsMap["google-map-place"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mapPlacePhotos(params: OperationParamsMap["google-map-place-photos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mapPlaceReviews(params: OperationParamsMap["google-map-place-reviews"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mapSearch(params: OperationParamsMap["google-map-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params: OperationParamsMap["google-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsSearch(params: OperationParamsMap["google-news-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  suggest(params: OperationParamsMap["google-suggest"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsCategories(params?: OperationParamsMap["google-trends-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsEnums(params?: OperationParamsMap["google-trends-enums"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsExplore(params: OperationParamsMap["google-trends-explore"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsExploreInterestByRegion(params: OperationParamsMap["google-trends-explore-interest-by-region"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsExploreInterestOverTime(params: OperationParamsMap["google-trends-explore-interest-over-time"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsExploreRelatedTopics(params: OperationParamsMap["google-trends-explore-related-topics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsExploreRisingQueries(params: OperationParamsMap["google-trends-explore-rising-queries"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsExploreTopQueries(params: OperationParamsMap["google-trends-explore-top-queries"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsLocations(params?: OperationParamsMap["google-trends-locations"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsTrending(params?: OperationParamsMap["google-trends-trending"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trendsTrendingDetail(params: OperationParamsMap["google-trends-trending-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  videos(params: OperationParamsMap["google-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeAnalystArticles(params: OperationParamsMap["google-finance-analyst-articles"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeChart(params: OperationParamsMap["google-finance-chart"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeClassification(params: OperationParamsMap["google-finance-classification"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeCompany(params: OperationParamsMap["google-finance-company"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeContext(params: OperationParamsMap["google-finance-context"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeFinancials(params: OperationParamsMap["google-finance-financials"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsCategoryNews(params: OperationParamsMap["google-finance-markets-category-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsCategoryStocks(params: OperationParamsMap["google-finance-markets-category-stocks"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsEarnings(params?: OperationParamsMap["google-finance-markets-earnings"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsFeatured(params?: OperationParamsMap["google-finance-markets-featured"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsHeadline(params?: OperationParamsMap["google-finance-markets-headline"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsIndices(params?: OperationParamsMap["google-finance-markets-indices"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsMovers(params?: OperationParamsMap["google-finance-markets-movers"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsTop(params?: OperationParamsMap["google-finance-markets-top"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeMarketsTrending(params?: OperationParamsMap["google-finance-markets-trending"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeNews(params: OperationParamsMap["google-finance-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeQuote(params: OperationParamsMap["google-finance-quote"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeRelated(params: OperationParamsMap["google-finance-related"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeSearch(params: OperationParamsMap["google-finance-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  financeTicker(params: OperationParamsMap["google-finance-ticker"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  jobs(params: OperationParamsMap["google-jobs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mapPlace(params: OperationParamsMap["google-map-place"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mapPlacePhotos(params: OperationParamsMap["google-map-place-photos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mapPlaceReviews(params: OperationParamsMap["google-map-place-reviews"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mapSearch(params: OperationParamsMap["google-map-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params: OperationParamsMap["google-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsSearch(params: OperationParamsMap["google-news-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  suggest(params: OperationParamsMap["google-suggest"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsCategories(params?: OperationParamsMap["google-trends-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsEnums(params?: OperationParamsMap["google-trends-enums"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsExplore(params: OperationParamsMap["google-trends-explore"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsExploreInterestByRegion(params: OperationParamsMap["google-trends-explore-interest-by-region"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsExploreInterestOverTime(params: OperationParamsMap["google-trends-explore-interest-over-time"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsExploreRelatedTopics(params: OperationParamsMap["google-trends-explore-related-topics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsExploreRisingQueries(params: OperationParamsMap["google-trends-explore-rising-queries"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsExploreTopQueries(params: OperationParamsMap["google-trends-explore-top-queries"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsLocations(params?: OperationParamsMap["google-trends-locations"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsTrending(params?: OperationParamsMap["google-trends-trending"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trendsTrendingDetail(params: OperationParamsMap["google-trends-trending-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  videos(params: OperationParamsMap["google-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  financeAnalystArticles(...args: OperationRequestArgs<"google-finance-analyst-articles">): Promise<OperationResponseMap["google-finance-analyst-articles"]>;
  financeChart(...args: OperationRequestArgs<"google-finance-chart">): Promise<OperationResponseMap["google-finance-chart"]>;
  financeClassification(...args: OperationRequestArgs<"google-finance-classification">): Promise<OperationResponseMap["google-finance-classification"]>;
  financeCompany(...args: OperationRequestArgs<"google-finance-company">): Promise<OperationResponseMap["google-finance-company"]>;
  financeContext(...args: OperationRequestArgs<"google-finance-context">): Promise<OperationResponseMap["google-finance-context"]>;
  financeFinancials(...args: OperationRequestArgs<"google-finance-financials">): Promise<OperationResponseMap["google-finance-financials"]>;
  financeMarketsCategoryNews(...args: OperationRequestArgs<"google-finance-markets-category-news">): Promise<OperationResponseMap["google-finance-markets-category-news"]>;
  financeMarketsCategoryStocks(...args: OperationRequestArgs<"google-finance-markets-category-stocks">): Promise<OperationResponseMap["google-finance-markets-category-stocks"]>;
  financeMarketsEarnings(...args: OperationRequestArgs<"google-finance-markets-earnings">): Promise<OperationResponseMap["google-finance-markets-earnings"]>;
  financeMarketsFeatured(...args: OperationRequestArgs<"google-finance-markets-featured">): Promise<OperationResponseMap["google-finance-markets-featured"]>;
  financeMarketsHeadline(...args: OperationRequestArgs<"google-finance-markets-headline">): Promise<OperationResponseMap["google-finance-markets-headline"]>;
  financeMarketsIndices(...args: OperationRequestArgs<"google-finance-markets-indices">): Promise<OperationResponseMap["google-finance-markets-indices"]>;
  financeMarketsMovers(...args: OperationRequestArgs<"google-finance-markets-movers">): Promise<OperationResponseMap["google-finance-markets-movers"]>;
  financeMarketsTop(...args: OperationRequestArgs<"google-finance-markets-top">): Promise<OperationResponseMap["google-finance-markets-top"]>;
  financeMarketsTrending(...args: OperationRequestArgs<"google-finance-markets-trending">): Promise<OperationResponseMap["google-finance-markets-trending"]>;
  financeNews(...args: OperationRequestArgs<"google-finance-news">): Promise<OperationResponseMap["google-finance-news"]>;
  financeQuote(...args: OperationRequestArgs<"google-finance-quote">): Promise<OperationResponseMap["google-finance-quote"]>;
  financeRelated(...args: OperationRequestArgs<"google-finance-related">): Promise<OperationResponseMap["google-finance-related"]>;
  financeSearch(...args: OperationRequestArgs<"google-finance-search">): Promise<OperationResponseMap["google-finance-search"]>;
  financeTicker(...args: OperationRequestArgs<"google-finance-ticker">): Promise<OperationResponseMap["google-finance-ticker"]>;
  jobs(...args: OperationRequestArgs<"google-jobs">): Promise<OperationResponseMap["google-jobs"]>;
  mapPlace(...args: OperationRequestArgs<"google-map-place">): Promise<OperationResponseMap["google-map-place"]>;
  mapPlacePhotos(...args: OperationRequestArgs<"google-map-place-photos">): Promise<OperationResponseMap["google-map-place-photos"]>;
  mapPlaceReviews(...args: OperationRequestArgs<"google-map-place-reviews">): Promise<OperationResponseMap["google-map-place-reviews"]>;
  mapSearch(...args: OperationRequestArgs<"google-map-search">): Promise<OperationResponseMap["google-map-search"]>;
  news(...args: OperationRequestArgs<"google-news">): Promise<OperationResponseMap["google-news"]>;
  newsSearch(...args: OperationRequestArgs<"google-news-search">): Promise<OperationResponseMap["google-news-search"]>;
  suggest(...args: OperationRequestArgs<"google-suggest">): Promise<OperationResponseMap["google-suggest"]>;
  trendsCategories(...args: OperationRequestArgs<"google-trends-categories">): Promise<OperationResponseMap["google-trends-categories"]>;
  trendsEnums(...args: OperationRequestArgs<"google-trends-enums">): Promise<OperationResponseMap["google-trends-enums"]>;
  trendsExplore(...args: OperationRequestArgs<"google-trends-explore">): Promise<OperationResponseMap["google-trends-explore"]>;
  trendsExploreInterestByRegion(...args: OperationRequestArgs<"google-trends-explore-interest-by-region">): Promise<OperationResponseMap["google-trends-explore-interest-by-region"]>;
  trendsExploreInterestOverTime(...args: OperationRequestArgs<"google-trends-explore-interest-over-time">): Promise<OperationResponseMap["google-trends-explore-interest-over-time"]>;
  trendsExploreRelatedTopics(...args: OperationRequestArgs<"google-trends-explore-related-topics">): Promise<OperationResponseMap["google-trends-explore-related-topics"]>;
  trendsExploreRisingQueries(...args: OperationRequestArgs<"google-trends-explore-rising-queries">): Promise<OperationResponseMap["google-trends-explore-rising-queries"]>;
  trendsExploreTopQueries(...args: OperationRequestArgs<"google-trends-explore-top-queries">): Promise<OperationResponseMap["google-trends-explore-top-queries"]>;
  trendsLocations(...args: OperationRequestArgs<"google-trends-locations">): Promise<OperationResponseMap["google-trends-locations"]>;
  trendsTrending(...args: OperationRequestArgs<"google-trends-trending">): Promise<OperationResponseMap["google-trends-trending"]>;
  trendsTrendingDetail(...args: OperationRequestArgs<"google-trends-trending-detail">): Promise<OperationResponseMap["google-trends-trending-detail"]>;
  videos(...args: OperationRequestArgs<"google-videos">): Promise<OperationResponseMap["google-videos"]>;
}
export { GoogleClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default GoogleClient;

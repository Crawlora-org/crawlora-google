"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class GoogleClient(CrawloraClient):
    """Synchronous Google API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-google-python/0.1.0')
        super().__init__(*args, **kwargs)

    def finance_analyst_articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-analyst-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_classification(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-classification', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_company(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-company', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_context(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-context', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_financials(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-financials', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_category_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-category-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_category_stocks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-category-stocks', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_earnings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-earnings', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_featured(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-featured', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_headline(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-headline', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_indices(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-indices', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_movers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-movers', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_top(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-top', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_markets_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-markets-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_quote(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-quote', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-related', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def finance_ticker(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-finance-ticker', params, response_type=response_type, timeout=timeout, headers=headers)

    def jobs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-jobs', params, response_type=response_type, timeout=timeout, headers=headers)

    def map_place(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-map-place', params, response_type=response_type, timeout=timeout, headers=headers)

    def map_place_photos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-map-place-photos', params, response_type=response_type, timeout=timeout, headers=headers)

    def map_place_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-map-place-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def map_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-map-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-news-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_explore(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-explore', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_explore_interest_by_region(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-explore-interest-by-region', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_explore_interest_over_time(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-explore-interest-over-time', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_explore_related_topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-explore-related-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_explore_rising_queries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-explore-rising-queries', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_explore_top_queries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-explore-top-queries', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends_trending_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-trends-trending-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('google-videos', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncGoogleClient(AsyncCrawloraClient):
    """Asynchronous Google API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-google-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def finance_analyst_articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-analyst-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_chart(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-chart', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_classification(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-classification', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_company(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-company', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_context(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-context', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_financials(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-financials', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_category_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-category-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_category_stocks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-category-stocks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_earnings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-earnings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_featured(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-featured', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_headline(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-headline', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_indices(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-indices', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_movers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-movers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_top(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-top', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_markets_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-markets-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_quote(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-quote', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-related', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def finance_ticker(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-finance-ticker', params, response_type=response_type, timeout=timeout, headers=headers)

    async def jobs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-jobs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def map_place(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-map-place', params, response_type=response_type, timeout=timeout, headers=headers)

    async def map_place_photos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-map-place-photos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def map_place_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-map-place-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def map_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-map-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-news-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_explore(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-explore', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_explore_interest_by_region(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-explore-interest-by-region', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_explore_interest_over_time(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-explore-interest-over-time', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_explore_related_topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-explore-related-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_explore_rising_queries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-explore-rising-queries', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_explore_top_queries(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-explore-top-queries', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends_trending_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-trends-trending-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('google-videos', params, response_type=response_type, timeout=timeout, headers=headers)

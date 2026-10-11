from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelGoogleVideosResponseDoc = TypedDict('ModelGoogleVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleVideosResponse = TypedDict('ModelGoogleVideosResponse', {
    'pagination': NotRequired[ModelGoogleVerticalPagination],
    'results': NotRequired[list[ModelGoogleVideoResult]],
}, total=False)

ModelGoogleVideoResult = TypedDict('ModelGoogleVideoResult', {
    'age': NotRequired[str],
    'description': NotRequired[str],
    'duration': NotRequired[str],
    'platform': NotRequired[str],
    'position': NotRequired[int],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGoogleVerticalPagination = TypedDict('ModelGoogleVerticalPagination', {
    'next_page': NotRequired[int],
    'page': NotRequired[int],
    'previous_page': NotRequired[int],
}, total=False)

ModelTrendsExploreResponseDoc = TypedDict('ModelTrendsExploreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsExploreResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsExploreResponse = TypedDict('ModelTrendsExploreResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'interest_by_region': NotRequired[list[ModelTrendsRegionInterest]],
    'interest_over_time': NotRequired[list[ModelTrendsInterestPoint]],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'related_queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'related_topics': NotRequired[list[ModelTrendsRelatedGroup]],
    'rising_queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'time_range': NotRequired[str],
    'top_queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsRelatedGroup = TypedDict('ModelTrendsRelatedGroup', {
    'items': NotRequired[list[ModelTrendsRelatedItem]],
    'keyword': NotRequired[str],
}, total=False)

ModelTrendsRelatedItem = TypedDict('ModelTrendsRelatedItem', {
    'formatted_value': NotRequired[str],
    'link': NotRequired[str],
    'query': NotRequired[str],
    'topic_mid': NotRequired[str],
    'topic_title': NotRequired[str],
    'topic_type': NotRequired[str],
    'value': NotRequired[int],
}, total=False)

ModelTrendsInterestPoint = TypedDict('ModelTrendsInterestPoint', {
    'formatted_axis_time': NotRequired[str],
    'formatted_time': NotRequired[str],
    'time': NotRequired[str],
    'values': NotRequired[list[ModelTrendsTrendValue]],
}, total=False)

ModelTrendsTrendValue = TypedDict('ModelTrendsTrendValue', {
    'formatted_value': NotRequired[str],
    'has_data': NotRequired[bool],
    'keyword': NotRequired[str],
    'value': NotRequired[int],
}, total=False)

ModelTrendsRegionInterest = TypedDict('ModelTrendsRegionInterest', {
    'geo_code': NotRequired[str],
    'geo_name': NotRequired[str],
    'values': NotRequired[list[ModelTrendsTrendValue]],
}, total=False)

ModelTrendsTrendingDetailRequest = TypedDict('ModelTrendsTrendingDetailRequest', {
    'category': NotRequired[int],
    'geo': NotRequired[Literal['WORLDWIDE', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CV', 'CA', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'property': NotRequired[str],
    'query': NotRequired[str],
    'time_range': NotRequired[Literal['now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m', 'today 5-y', 'all']],
    'type': NotRequired[Literal['web', 'image', 'news', 'youtube', 'shopping']],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsTrendingResponseDoc = TypedDict('ModelTrendsTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendingResponse = TypedDict('ModelTrendsTrendingResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'items': NotRequired[list[ModelTrendsTrendingItem]],
    'sort_by': NotRequired[str],
    'status': NotRequired[str],
    'time_range': NotRequired[str],
    'tz': NotRequired[int],
    'window': NotRequired[str],
}, total=False)

ModelTrendsTrendingItem = TypedDict('ModelTrendsTrendingItem', {
    'articles': NotRequired[list[ModelTrendsTrendingArticle]],
    'explore_url': NotRequired[str],
    'query': NotRequired[str],
    'rank': NotRequired[int],
    'related_terms': NotRequired[list[str]],
    'share_url': NotRequired[str],
    'started_unix': NotRequired[int],
    'status': NotRequired[str],
    'title': NotRequired[str],
    'traffic': NotRequired[str],
    'updated_unix': NotRequired[int],
}, total=False)

ModelTrendsTrendingArticle = TypedDict('ModelTrendsTrendingArticle', {
    'source': NotRequired[str],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelTrendsTrendsLocationsResponseDoc = TypedDict('ModelTrendsTrendsLocationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendsLocationsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendsLocationsResponse = TypedDict('ModelTrendsTrendsLocationsResponse', {
    'locations': NotRequired[list[str]],
}, total=False)

ModelTrendsExploreQueriesResponseDoc = TypedDict('ModelTrendsExploreQueriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsExploreQueriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsExploreQueriesResponse = TypedDict('ModelTrendsExploreQueriesResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'queries': NotRequired[list[ModelTrendsRelatedGroup]],
    'query_type': NotRequired[str],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsExploreRequest = TypedDict('ModelTrendsExploreRequest', {
    'category': NotRequired[int],
    'geo': NotRequired[Literal['WORLDWIDE', 'AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'time_range': NotRequired[Literal['now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', 'today 3-m', 'today 12-m', 'today 5-y', 'all']],
    'type': NotRequired[Literal['web', 'image', 'news', 'youtube', 'shopping']],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsRelatedTopicsResponseDoc = TypedDict('ModelTrendsRelatedTopicsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsRelatedTopicsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsRelatedTopicsResponse = TypedDict('ModelTrendsRelatedTopicsResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'related_topics': NotRequired[list[ModelTrendsRelatedGroup]],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsInterestOverTimeResponseDoc = TypedDict('ModelTrendsInterestOverTimeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsInterestOverTimeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsInterestOverTimeResponse = TypedDict('ModelTrendsInterestOverTimeResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'interest_over_time': NotRequired[list[ModelTrendsInterestPoint]],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsInterestByRegionResponseDoc = TypedDict('ModelTrendsInterestByRegionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsInterestByRegionResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsInterestByRegionResponse = TypedDict('ModelTrendsInterestByRegionResponse', {
    'category': NotRequired[int],
    'geo': NotRequired[str],
    'hl': NotRequired[str],
    'interest_by_region': NotRequired[list[ModelTrendsRegionInterest]],
    'keywords': NotRequired[list[str]],
    'property': NotRequired[str],
    'time_range': NotRequired[str],
    'type': NotRequired[str],
    'tz': NotRequired[int],
}, total=False)

ModelTrendsTrendsEnumsResponseDoc = TypedDict('ModelTrendsTrendsEnumsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendsEnumsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendsEnumsResponse = TypedDict('ModelTrendsTrendsEnumsResponse', {
    'explore_time_ranges': NotRequired[list[str]],
    'locations': NotRequired[list[str]],
    'search_types': NotRequired[list[str]],
    'trend_statuses': NotRequired[list[str]],
    'trending_categories': NotRequired[list[ModelTrendsTrendCategory]],
    'trending_sort_bys': NotRequired[list[str]],
    'trending_time_ranges': NotRequired[list[str]],
}, total=False)

ModelTrendsTrendCategory = TypedDict('ModelTrendsTrendCategory', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelTrendsTrendsCategoriesResponseDoc = TypedDict('ModelTrendsTrendsCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTrendsTrendsCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTrendsTrendsCategoriesResponse = TypedDict('ModelTrendsTrendsCategoriesResponse', {
    'categories': NotRequired[list[ModelTrendsTrendCategory]],
}, total=False)

ModelGoogleSuggestResponseDoc = TypedDict('ModelGoogleSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleSuggestResponse = TypedDict('ModelGoogleSuggestResponse', {
    'query': NotRequired[str],
    'source': NotRequired[str],
    'suggestions': NotRequired[list[ModelGoogleSuggestionResult]],
}, total=False)

ModelGoogleSuggestionResult = TypedDict('ModelGoogleSuggestionResult', {
    'description': NotRequired[str],
    'position': NotRequired[int],
    'query': NotRequired[str],
    'relevance': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelGoogleNewsSearchResponseDoc = TypedDict('ModelGoogleNewsSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleNewsSearchResp],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleNewsSearchResp = TypedDict('ModelGoogleNewsSearchResp', {
    'result': NotRequired[list[ModelGoogleSearchItem]],
}, total=False)

ModelGoogleSearchItem = TypedDict('ModelGoogleSearchItem', {
    'Snippet': NotRequired[str],
    'icon': NotRequired[str],
    'link': NotRequired[str],
    'position': NotRequired[int],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'website_name': NotRequired[str],
}, total=False)

ModelGoogleSearchOption = TypedDict('ModelGoogleSearchOption', {
    'country': Required[str],
    'keyword': Required[str],
    'language': Required[str],
    'limit': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

ModelGoogleNewsResponseDoc = TypedDict('ModelGoogleNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleNewsResponse = TypedDict('ModelGoogleNewsResponse', {
    'pagination': NotRequired[ModelGoogleVerticalPagination],
    'results': NotRequired[list[ModelGoogleNewsResult]],
}, total=False)

ModelGoogleNewsResult = TypedDict('ModelGoogleNewsResult', {
    'age': NotRequired[str],
    'description': NotRequired[str],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGoogleMapSearchResponseDoc = TypedDict('ModelGoogleMapSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelGooglePlace]],
    'msg': NotRequired[str],
}, total=False)

ModelGooglePlace = TypedDict('ModelGooglePlace', {
    'address': NotRequired[str],
    'amenities': NotRequired[list[str]],
    'category': NotRequired[list[str]],
    'description': NotRequired[str],
    'image': NotRequired[str],
    'latitude': NotRequired[float],
    'locations': NotRequired[list[str]],
    'longitude': NotRequired[float],
    'name': NotRequired[str],
    'phone': NotRequired[str],
    'place_id': NotRequired[str],
    'rating': NotRequired[float | None],
    'review_count': NotRequired[int],
    'url': NotRequired[str],
    'website': NotRequired[str],
}, total=False)

ModelGoogleMapSearchOption = TypedDict('ModelGoogleMapSearchOption', {
    'country': NotRequired[str],
    'keyword': NotRequired[str],
    'language': NotRequired[str],
}, total=False)

ModelGoogleMapPlaceReviewsResponseDoc = TypedDict('ModelGoogleMapPlaceReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelGooglePlaceReview]],
    'msg': NotRequired[str],
}, total=False)

ModelGooglePlaceReview = TypedDict('ModelGooglePlaceReview', {
    'author_id': NotRequired[str],
    'author_name': NotRequired[str],
    'author_photo': NotRequired[str],
    'author_review_count': NotRequired[int],
    'author_url': NotRequired[str],
    'id': NotRequired[str],
    'photos': NotRequired[list[ModelGooglePlacePhoto]],
    'published_at': NotRequired[str],
    'rating': NotRequired[int],
    'relative_time': NotRequired[str],
    'source': NotRequired[str],
    'text': NotRequired[str],
}, total=False)

ModelGooglePlacePhoto = TypedDict('ModelGooglePlacePhoto', {
    'height': NotRequired[int],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelGoogleMapPlacePhotosResponseDoc = TypedDict('ModelGoogleMapPlacePhotosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelGooglePlacePhoto]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleMapPlaceResponseDoc = TypedDict('ModelGoogleMapPlaceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGooglePlace],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleJobsResponse = TypedDict('ModelGoogleJobsResponse', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelGoogleJobItem]],
}, total=False)

ModelGoogleJobItem = TypedDict('ModelGoogleJobItem', {
    'company': NotRequired[str],
    'employment': NotRequired[str],
    'location': NotRequired[str],
    'posted_at': NotRequired[str],
    'snippet': NotRequired[str],
    'source': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGoogleJobsOption = TypedDict('ModelGoogleJobsOption', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'query': Required[str],
}, total=False)

ModelFinanceTickerResponseDoc = TypedDict('ModelFinanceTickerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceTicker]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceTicker = TypedDict('ModelFinanceTicker', {
    'price': NotRequired[float],
    'time': NotRequired[str],
    'volume': NotRequired[int],
}, total=False)

ModelFinanceSearchResponseDoc = TypedDict('ModelFinanceSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceStockData]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceStockData = TypedDict('ModelFinanceStockData', {
    'change': NotRequired[float],
    'company_name': NotRequired[str],
    'currency': NotRequired[str],
    'exchange': NotRequired[str],
    'percentage': NotRequired[float],
    'price': NotRequired[float],
    'ticker': NotRequired[str],
}, total=False)

ModelFinanceRelatedResponseDoc = TypedDict('ModelFinanceRelatedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceRelatedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceRelatedResponse = TypedDict('ModelFinanceRelatedResponse', {
    'instrument': NotRequired[ModelFinanceInstrument],
    'items': NotRequired[list[ModelFinanceInstrument]],
}, total=False)

ModelFinanceInstrument = TypedDict('ModelFinanceInstrument', {
    'after_hours': NotRequired[ModelFinancePriceChange],
    'change': NotRequired[float],
    'change_percent': NotRequired[float],
    'country': NotRequired[str],
    'currency': NotRequired[str],
    'exchange': NotRequired[str],
    'google_id': NotRequired[str],
    'identifier': NotRequired[str],
    'last_update_unix': NotRequired[int],
    'name': NotRequired[str],
    'previous_close': NotRequired[float],
    'price': NotRequired[float],
    'ticker': NotRequired[str],
    'timezone': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFinancePriceChange = TypedDict('ModelFinancePriceChange', {
    'change': NotRequired[float],
    'change_percent': NotRequired[float],
    'price': NotRequired[float],
}, total=False)

ModelFinanceQuoteResponseDoc = TypedDict('ModelFinanceQuoteResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceQuoteResp],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceQuoteResp = TypedDict('ModelFinanceQuoteResp', {
    'about': NotRequired[ModelFinanceAbout],
    'investment': NotRequired[ModelFinanceInvestment],
    'key_stats': NotRequired[ModelFinanceKeyStats],
    'news': NotRequired[list[ModelFinanceNews]],
    'tickers': NotRequired[list[ModelFinanceTicker]],
    'title': NotRequired[str],
}, total=False)

ModelFinanceNews = TypedDict('ModelFinanceNews', {
    'source': NotRequired[str],
    'time': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFinanceKeyStats = TypedDict('ModelFinanceKeyStats', {
    'avg_volume': NotRequired[int],
    'climate_change_score': NotRequired[str],
    'currency': NotRequired[str],
    'day_range': NotRequired[ModelFinanceRange],
    'dividend_yield': NotRequired[float],
    'market_cap': NotRequired[int],
    'pe_ratio': NotRequired[float],
    'previous_close': NotRequired[float],
    'primary_exchange': NotRequired[str],
    'tags': NotRequired[list[str]],
    'year_range': NotRequired[ModelFinanceRange],
}, total=False)

ModelFinanceRange = TypedDict('ModelFinanceRange', {
    'from': NotRequired[float],
    'to': NotRequired[float],
}, total=False)

ModelFinanceInvestment = TypedDict('ModelFinanceInvestment', {
    'balance_sheet': NotRequired[list[ModelFinanceBalanceSheet]],
    'cash_flow': NotRequired[list[ModelFinanceCashFlow]],
    'income_statement': NotRequired[list[ModelFinanceIncomeStatement]],
}, total=False)

ModelFinanceIncomeStatement = TypedDict('ModelFinanceIncomeStatement', {
    'earnings_per_share': NotRequired[float],
    'earnings_per_share_change_yy': NotRequired[float],
    'ebitda': NotRequired[float],
    'ebitda_change_yy': NotRequired[float],
    'effective_tax_rate': NotRequired[float],
    'net_income': NotRequired[float],
    'net_income_change_yy': NotRequired[float],
    'net_profit_margin': NotRequired[float],
    'net_profit_margin_change_yy': NotRequired[float],
    'operating_expense': NotRequired[float],
    'operating_expense_change_yy': NotRequired[float],
    'quarter': NotRequired[int],
    'revenue': NotRequired[float],
    'revenue_change_yy': NotRequired[float],
    'year': NotRequired[int],
}, total=False)

ModelFinanceCashFlow = TypedDict('ModelFinanceCashFlow', {
    'cash_from_financing': NotRequired[float],
    'cash_from_financing_change_yy': NotRequired[float],
    'cash_from_investing': NotRequired[float],
    'cash_from_investing_change_yy': NotRequired[float],
    'cash_from_operations': NotRequired[float],
    'cash_from_operations_change_yy': NotRequired[float],
    'free_cash_flow': NotRequired[float],
    'free_cash_flow_change_yy': NotRequired[float],
    'net_change_in_cash': NotRequired[float],
    'net_change_in_cash_change_yy': NotRequired[float],
    'net_income': NotRequired[float],
    'net_income_change_yy': NotRequired[float],
    'quarter': NotRequired[int],
    'year': NotRequired[int],
}, total=False)

ModelFinanceBalanceSheet = TypedDict('ModelFinanceBalanceSheet', {
    'cash_and_short_term_change_yy': NotRequired[float],
    'cash_and_short_term_investments': NotRequired[float],
    'price_to_book': NotRequired[float],
    'quarter': NotRequired[int],
    'return_on_assets': NotRequired[float],
    'return_on_capital': NotRequired[float],
    'shares_outstanding': NotRequired[float],
    'total_assets': NotRequired[float],
    'total_assets_change_yy': NotRequired[float],
    'total_equity': NotRequired[float],
    'total_liabilities': NotRequired[float],
    'total_liabilities_change_yy': NotRequired[float],
    'year': NotRequired[int],
}, total=False)

ModelFinanceAbout = TypedDict('ModelFinanceAbout', {
    'about': NotRequired[str],
    'ceo': NotRequired[str],
    'employees': NotRequired[int],
    'founded': NotRequired[str],
    'headquarters': NotRequired[str],
    'website': NotRequired[str],
}, total=False)

ModelFinanceArticlesResponseDoc = TypedDict('ModelFinanceArticlesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceFinanceArticle]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceFinanceArticle = TypedDict('ModelFinanceFinanceArticle', {
    'published_at': NotRequired[str],
    'published_unix': NotRequired[int],
    'related': NotRequired[list[ModelFinanceInstrument]],
    'source': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFinanceInstrumentsResponseDoc = TypedDict('ModelFinanceInstrumentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelFinanceInstrument]],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceTopStocksResponseDoc = TypedDict('ModelFinanceTopStocksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceTopStocksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceTopStocksResponse = TypedDict('ModelFinanceTopStocksResponse', {
    'items': NotRequired[list[ModelFinanceInstrument]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

ModelFinanceMarketMoversResponseDoc = TypedDict('ModelFinanceMarketMoversResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceMarketMoversResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceMarketMoversResponse = TypedDict('ModelFinanceMarketMoversResponse', {
    'categories': NotRequired[list[int]],
    'count': NotRequired[int],
    'items': NotRequired[list[ModelFinanceInstrument]],
    'offset': NotRequired[int],
}, total=False)

ModelFinanceHeadlineResponseDoc = TypedDict('ModelFinanceHeadlineResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceHeadlineResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceHeadlineResponse = TypedDict('ModelFinanceHeadlineResponse', {
    'article': NotRequired[ModelFinanceFinanceArticle],
}, total=False)

ModelFinanceEarningsResponseDoc = TypedDict('ModelFinanceEarningsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceEarningsCalendarResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceEarningsCalendarResponse = TypedDict('ModelFinanceEarningsCalendarResponse', {
    'items': NotRequired[list[ModelFinanceEarningsEvent]],
}, total=False)

ModelFinanceEarningsEvent = TypedDict('ModelFinanceEarningsEvent', {
    'company_name': NotRequired[str],
    'conference_phone': NotRequired[str],
    'conference_url': NotRequired[str],
    'event_time': NotRequired[str],
    'event_unix': NotRequired[int],
    'fiscal_period': NotRequired[str],
    'instrument': NotRequired[ModelFinanceInstrument],
}, total=False)

ModelFinanceCategoryStocksResponseDoc = TypedDict('ModelFinanceCategoryStocksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceCategoryStocksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceCategoryStocksResponse = TypedDict('ModelFinanceCategoryStocksResponse', {
    'category': NotRequired[str],
    'items': NotRequired[list[ModelFinanceInstrument]],
    'offset': NotRequired[int],
}, total=False)

ModelFinanceCategoryNewsResponseDoc = TypedDict('ModelFinanceCategoryNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceCategoryNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceCategoryNewsResponse = TypedDict('ModelFinanceCategoryNewsResponse', {
    'category': NotRequired[str],
    'items': NotRequired[list[ModelFinanceFinanceArticle]],
    'offset': NotRequired[int],
}, total=False)

ModelFinanceFinancialsResponseDoc = TypedDict('ModelFinanceFinancialsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceFinancialsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceFinancialsResponse = TypedDict('ModelFinanceFinancialsResponse', {
    'annual': NotRequired[list[ModelFinanceFinancialPeriod]],
    'currency': NotRequired[str],
    'quarterly': NotRequired[list[ModelFinanceFinancialPeriod]],
}, total=False)

ModelFinanceFinancialPeriod = TypedDict('ModelFinanceFinancialPeriod', {
    'capital_expenditure': NotRequired[float],
    'ebitda': NotRequired[float],
    'eps': NotRequired[float],
    'eps_diluted': NotRequired[float],
    'free_cash_flow': NotRequired[float],
    'net_income': NotRequired[float],
    'operating_cash_flow': NotRequired[float],
    'operating_income': NotRequired[float],
    'operating_margin': NotRequired[float],
    'pe_ratio': NotRequired[float],
    'period': NotRequired[str],
    'period_end': NotRequired[str],
    'profit_margin': NotRequired[float],
    'revenue': NotRequired[float],
    'revenue_growth_yoy': NotRequired[float],
    'shares_outstanding': NotRequired[float],
    'total_assets': NotRequired[float],
    'total_equity': NotRequired[float],
    'total_liabilities': NotRequired[float],
}, total=False)

ModelFinanceContextResponseDoc = TypedDict('ModelFinanceContextResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceContextResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceContextResponse = TypedDict('ModelFinanceContextResponse', {
    'items': NotRequired[list[ModelFinanceInstrument]],
    'query': NotRequired[str],
}, total=False)

ModelFinanceCompanyResponseDoc = TypedDict('ModelFinanceCompanyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceCompanyInfo],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceCompanyInfo = TypedDict('ModelFinanceCompanyInfo', {
    'ceo': NotRequired[str],
    'description': NotRequired[str],
    'employees': NotRequired[int],
    'fifty_two_week_high': NotRequired[float],
    'fifty_two_week_low': NotRequired[float],
    'headquarters': NotRequired[str],
    'high': NotRequired[float],
    'low': NotRequired[float],
    'market_cap': NotRequired[float],
    'open': NotRequired[float],
    'pe_ratio': NotRequired[float],
    'sector': NotRequired[str],
    'volume': NotRequired[int],
}, total=False)

ModelFinanceClassificationResponseDoc = TypedDict('ModelFinanceClassificationResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceClassificationResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceClassificationResponse = TypedDict('ModelFinanceClassificationResponse', {
    'categories': NotRequired[list[str]],
    'instrument': NotRequired[ModelFinanceInstrument],
}, total=False)

ModelFinanceChartResponseDoc = TypedDict('ModelFinanceChartResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFinanceChartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelFinanceChartResponse = TypedDict('ModelFinanceChartResponse', {
    'instrument': NotRequired[ModelFinanceInstrument],
    'points': NotRequired[list[ModelFinanceTicker]],
    'previous_close': NotRequired[float],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceAnalystArticlesResponse = ModelFinanceArticlesResponseDoc
GoogleFinanceAnalystArticlesParams = TypedDict('GoogleFinanceAnalystArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceChartResponse = ModelFinanceChartResponseDoc
GoogleFinanceChartParams = TypedDict('GoogleFinanceChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceClassificationResponse = ModelFinanceClassificationResponseDoc
GoogleFinanceClassificationParams = TypedDict('GoogleFinanceClassificationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceCompanyResponse = ModelFinanceCompanyResponseDoc
GoogleFinanceCompanyParams = TypedDict('GoogleFinanceCompanyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceContextResponse = ModelFinanceContextResponseDoc
GoogleFinanceContextParams = TypedDict('GoogleFinanceContextParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

GoogleFinanceFinancialsResponse = ModelFinanceFinancialsResponseDoc
GoogleFinanceFinancialsParams = TypedDict('GoogleFinanceFinancialsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceMarketsCategoryNewsResponse = ModelFinanceCategoryNewsResponseDoc
GoogleFinanceMarketsCategoryNewsParams = TypedDict('GoogleFinanceMarketsCategoryNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryStocksResponse = ModelFinanceCategoryStocksResponseDoc
GoogleFinanceMarketsCategoryStocksParams = TypedDict('GoogleFinanceMarketsCategoryStocksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsEarningsResponse = ModelFinanceEarningsResponseDoc
GoogleFinanceMarketsEarningsParams = TypedDict('GoogleFinanceMarketsEarningsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsFeaturedResponse = ModelFinanceInstrumentsResponseDoc
GoogleFinanceMarketsFeaturedParams = TypedDict('GoogleFinanceMarketsFeaturedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsHeadlineResponse = ModelFinanceHeadlineResponseDoc
GoogleFinanceMarketsHeadlineParams = TypedDict('GoogleFinanceMarketsHeadlineParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsIndicesResponse = ModelFinanceInstrumentsResponseDoc
GoogleFinanceMarketsIndicesParams = TypedDict('GoogleFinanceMarketsIndicesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleFinanceMarketsMoversResponse = ModelFinanceMarketMoversResponseDoc
GoogleFinanceMarketsMoversParams = TypedDict('GoogleFinanceMarketsMoversParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'categories': NotRequired[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTopResponse = ModelFinanceTopStocksResponseDoc
GoogleFinanceMarketsTopParams = TypedDict('GoogleFinanceMarketsTopParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTrendingResponse = ModelFinanceInstrumentsResponseDoc
GoogleFinanceMarketsTrendingParams = TypedDict('GoogleFinanceMarketsTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceNewsResponse = ModelFinanceArticlesResponseDoc
GoogleFinanceNewsParams = TypedDict('GoogleFinanceNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceQuoteResponse = ModelFinanceQuoteResponseDoc
GoogleFinanceQuoteParams = TypedDict('GoogleFinanceQuoteParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceRelatedResponse = ModelFinanceRelatedResponseDoc
GoogleFinanceRelatedParams = TypedDict('GoogleFinanceRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'quote': Required[str],
}, total=False)

GoogleFinanceSearchResponse = ModelFinanceSearchResponseDoc
GoogleFinanceSearchParams = TypedDict('GoogleFinanceSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

GoogleFinanceTickerResponse = ModelFinanceTickerResponseDoc
GoogleFinanceTickerParams = TypedDict('GoogleFinanceTickerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ticker': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleJobsBody = ModelGoogleJobsOption
GoogleJobsResponse = ModelGoogleJobsResponse
GoogleJobsParams = TypedDict('GoogleJobsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'option': Required[GoogleJobsBody],
}, total=False)

GoogleMapPlaceResponse = ModelGoogleMapPlaceResponseDoc
GoogleMapPlaceParams = TypedDict('GoogleMapPlaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'place_id': Required[str],
}, total=False)

GoogleMapPlacePhotosResponse = ModelGoogleMapPlacePhotosResponseDoc
GoogleMapPlacePhotosParams = TypedDict('GoogleMapPlacePhotosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapPlaceReviewsResponse = ModelGoogleMapPlaceReviewsResponseDoc
GoogleMapPlaceReviewsParams = TypedDict('GoogleMapPlaceReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapSearchBody = ModelGoogleMapSearchOption
GoogleMapSearchResponse = ModelGoogleMapSearchResponseDoc
GoogleMapSearchParams = TypedDict('GoogleMapSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mapSearchOption': Required[GoogleMapSearchBody],
}, total=False)

GoogleNewsResponse = ModelGoogleNewsResponseDoc
GoogleNewsParams = TypedDict('GoogleNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleNewsSearchBody = ModelGoogleSearchOption
GoogleNewsSearchResponse = ModelGoogleNewsSearchResponseDoc
GoogleNewsSearchParams = TypedDict('GoogleNewsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'searchOption': Required[GoogleNewsSearchBody],
}, total=False)

GoogleSuggestResponse = ModelGoogleSuggestResponseDoc
GoogleSuggestParams = TypedDict('GoogleSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'source': NotRequired[Literal['web', 'youtube', 'shopping']],
    'rich': NotRequired[bool],
}, total=False)

GoogleTrendsCategoriesResponse = ModelTrendsTrendsCategoriesResponseDoc
GoogleTrendsCategoriesParams = TypedDict('GoogleTrendsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsEnumsResponse = ModelTrendsTrendsEnumsResponseDoc
GoogleTrendsEnumsParams = TypedDict('GoogleTrendsEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsExploreBody = ModelTrendsExploreRequest
GoogleTrendsExploreResponse = ModelTrendsExploreResponseDoc
GoogleTrendsExploreParams = TypedDict('GoogleTrendsExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreBody],
}, total=False)

GoogleTrendsExploreInterestByRegionBody = ModelTrendsExploreRequest
GoogleTrendsExploreInterestByRegionResponse = ModelTrendsInterestByRegionResponseDoc
GoogleTrendsExploreInterestByRegionParams = TypedDict('GoogleTrendsExploreInterestByRegionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreInterestByRegionBody],
}, total=False)

GoogleTrendsExploreInterestOverTimeBody = ModelTrendsExploreRequest
GoogleTrendsExploreInterestOverTimeResponse = ModelTrendsInterestOverTimeResponseDoc
GoogleTrendsExploreInterestOverTimeParams = TypedDict('GoogleTrendsExploreInterestOverTimeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreInterestOverTimeBody],
}, total=False)

GoogleTrendsExploreRelatedTopicsBody = ModelTrendsExploreRequest
GoogleTrendsExploreRelatedTopicsResponse = ModelTrendsRelatedTopicsResponseDoc
GoogleTrendsExploreRelatedTopicsParams = TypedDict('GoogleTrendsExploreRelatedTopicsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreRelatedTopicsBody],
}, total=False)

GoogleTrendsExploreRisingQueriesBody = ModelTrendsExploreRequest
GoogleTrendsExploreRisingQueriesResponse = ModelTrendsExploreQueriesResponseDoc
GoogleTrendsExploreRisingQueriesParams = TypedDict('GoogleTrendsExploreRisingQueriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreRisingQueriesBody],
}, total=False)

GoogleTrendsExploreTopQueriesBody = ModelTrendsExploreRequest
GoogleTrendsExploreTopQueriesResponse = ModelTrendsExploreQueriesResponseDoc
GoogleTrendsExploreTopQueriesParams = TypedDict('GoogleTrendsExploreTopQueriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsExploreTopQueriesBody],
}, total=False)

GoogleTrendsLocationsResponse = ModelTrendsTrendsLocationsResponseDoc
GoogleTrendsLocationsParams = TypedDict('GoogleTrendsLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GoogleTrendsTrendingResponse = ModelTrendsTrendingResponseDoc
GoogleTrendsTrendingParams = TypedDict('GoogleTrendsTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'geo': NotRequired[Literal['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'tz': NotRequired[int],
    'window': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'time_range': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'category': NotRequired[Literal['0', '3', '47', '44', '22', '12', '5', '7', '71', '8', '45', '65', '11', '13', '958', '19', '16', '299', '14', '66', '29', '533', '174', '18', '20', '67']],
    'status': NotRequired[Literal['all', 'active', 'ended']],
    'sort_by': NotRequired[Literal['relevance', 'title', 'recency', 'search_volume']],
    'limit': NotRequired[int],
}, total=False)

GoogleTrendsTrendingDetailBody = ModelTrendsTrendingDetailRequest
GoogleTrendsTrendingDetailResponse = ModelTrendsExploreResponseDoc
GoogleTrendsTrendingDetailParams = TypedDict('GoogleTrendsTrendingDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'request': Required[GoogleTrendsTrendingDetailBody],
}, total=False)

GoogleVideosResponse = ModelGoogleVideosResponseDoc
GoogleVideosParams = TypedDict('GoogleVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

class GoogleGroup:
    @overload
    def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesTextResponseParams]) -> str: ...
    @overload
    def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesDefaultParams]) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    def finance_chart(self, **params: Unpack[GoogleFinanceChartStreamParams]) -> BinaryIO: ...
    @overload
    def finance_chart(self, **params: Unpack[GoogleFinanceChartTextResponseParams]) -> str: ...
    @overload
    def finance_chart(self, **params: Unpack[GoogleFinanceChartDefaultParams]) -> GoogleFinanceChartResponse: ...
    @overload
    def finance_classification(self, **params: Unpack[GoogleFinanceClassificationStreamParams]) -> BinaryIO: ...
    @overload
    def finance_classification(self, **params: Unpack[GoogleFinanceClassificationTextResponseParams]) -> str: ...
    @overload
    def finance_classification(self, **params: Unpack[GoogleFinanceClassificationDefaultParams]) -> GoogleFinanceClassificationResponse: ...
    @overload
    def finance_company(self, **params: Unpack[GoogleFinanceCompanyStreamParams]) -> BinaryIO: ...
    @overload
    def finance_company(self, **params: Unpack[GoogleFinanceCompanyTextResponseParams]) -> str: ...
    @overload
    def finance_company(self, **params: Unpack[GoogleFinanceCompanyDefaultParams]) -> GoogleFinanceCompanyResponse: ...
    @overload
    def finance_context(self, **params: Unpack[GoogleFinanceContextStreamParams]) -> BinaryIO: ...
    @overload
    def finance_context(self, **params: Unpack[GoogleFinanceContextTextResponseParams]) -> str: ...
    @overload
    def finance_context(self, **params: Unpack[GoogleFinanceContextDefaultParams]) -> GoogleFinanceContextResponse: ...
    @overload
    def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsTextResponseParams]) -> str: ...
    @overload
    def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsDefaultParams]) -> GoogleFinanceFinancialsResponse: ...
    @overload
    def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsTextResponseParams]) -> str: ...
    @overload
    def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsDefaultParams]) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksTextResponseParams]) -> str: ...
    @overload
    def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksDefaultParams]) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsTextResponseParams]) -> str: ...
    @overload
    def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsDefaultParams]) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedTextResponseParams]) -> str: ...
    @overload
    def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedDefaultParams]) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineTextResponseParams]) -> str: ...
    @overload
    def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineDefaultParams]) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesTextResponseParams]) -> str: ...
    @overload
    def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesDefaultParams]) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversTextResponseParams]) -> str: ...
    @overload
    def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversDefaultParams]) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopTextResponseParams]) -> str: ...
    @overload
    def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopDefaultParams]) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingTextResponseParams]) -> str: ...
    @overload
    def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingDefaultParams]) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    def finance_news(self, **params: Unpack[GoogleFinanceNewsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_news(self, **params: Unpack[GoogleFinanceNewsTextResponseParams]) -> str: ...
    @overload
    def finance_news(self, **params: Unpack[GoogleFinanceNewsDefaultParams]) -> GoogleFinanceNewsResponse: ...
    @overload
    def finance_quote(self, **params: Unpack[GoogleFinanceQuoteStreamParams]) -> BinaryIO: ...
    @overload
    def finance_quote(self, **params: Unpack[GoogleFinanceQuoteTextResponseParams]) -> str: ...
    @overload
    def finance_quote(self, **params: Unpack[GoogleFinanceQuoteDefaultParams]) -> GoogleFinanceQuoteResponse: ...
    @overload
    def finance_related(self, **params: Unpack[GoogleFinanceRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def finance_related(self, **params: Unpack[GoogleFinanceRelatedTextResponseParams]) -> str: ...
    @overload
    def finance_related(self, **params: Unpack[GoogleFinanceRelatedDefaultParams]) -> GoogleFinanceRelatedResponse: ...
    @overload
    def finance_search(self, **params: Unpack[GoogleFinanceSearchStreamParams]) -> BinaryIO: ...
    @overload
    def finance_search(self, **params: Unpack[GoogleFinanceSearchTextResponseParams]) -> str: ...
    @overload
    def finance_search(self, **params: Unpack[GoogleFinanceSearchDefaultParams]) -> GoogleFinanceSearchResponse: ...
    @overload
    def finance_ticker(self, **params: Unpack[GoogleFinanceTickerStreamParams]) -> BinaryIO: ...
    @overload
    def finance_ticker(self, **params: Unpack[GoogleFinanceTickerTextResponseParams]) -> str: ...
    @overload
    def finance_ticker(self, **params: Unpack[GoogleFinanceTickerDefaultParams]) -> GoogleFinanceTickerResponse: ...
    @overload
    def jobs(self, **params: Unpack[GoogleJobsStreamParams]) -> BinaryIO: ...
    @overload
    def jobs(self, **params: Unpack[GoogleJobsTextResponseParams]) -> str: ...
    @overload
    def jobs(self, **params: Unpack[GoogleJobsDefaultParams]) -> GoogleJobsResponse: ...
    @overload
    def map_place(self, **params: Unpack[GoogleMapPlaceStreamParams]) -> BinaryIO: ...
    @overload
    def map_place(self, **params: Unpack[GoogleMapPlaceTextResponseParams]) -> str: ...
    @overload
    def map_place(self, **params: Unpack[GoogleMapPlaceDefaultParams]) -> GoogleMapPlaceResponse: ...
    @overload
    def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosTextResponseParams]) -> str: ...
    @overload
    def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosDefaultParams]) -> GoogleMapPlacePhotosResponse: ...
    @overload
    def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsTextResponseParams]) -> str: ...
    @overload
    def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsDefaultParams]) -> GoogleMapPlaceReviewsResponse: ...
    @overload
    def map_search(self, **params: Unpack[GoogleMapSearchStreamParams]) -> BinaryIO: ...
    @overload
    def map_search(self, **params: Unpack[GoogleMapSearchTextResponseParams]) -> str: ...
    @overload
    def map_search(self, **params: Unpack[GoogleMapSearchDefaultParams]) -> GoogleMapSearchResponse: ...
    @overload
    def news(self, **params: Unpack[GoogleNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[GoogleNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[GoogleNewsDefaultParams]) -> GoogleNewsResponse: ...
    @overload
    def news_search(self, **params: Unpack[GoogleNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def news_search(self, **params: Unpack[GoogleNewsSearchTextResponseParams]) -> str: ...
    @overload
    def news_search(self, **params: Unpack[GoogleNewsSearchDefaultParams]) -> GoogleNewsSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[GoogleSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[GoogleSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[GoogleSuggestDefaultParams]) -> GoogleSuggestResponse: ...
    @overload
    def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesTextResponseParams]) -> str: ...
    @overload
    def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesDefaultParams]) -> GoogleTrendsCategoriesResponse: ...
    @overload
    def trends_enums(self, **params: Unpack[GoogleTrendsEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def trends_enums(self, **params: Unpack[GoogleTrendsEnumsTextResponseParams]) -> str: ...
    @overload
    def trends_enums(self, **params: Unpack[GoogleTrendsEnumsDefaultParams]) -> GoogleTrendsEnumsResponse: ...
    @overload
    def trends_explore(self, **params: Unpack[GoogleTrendsExploreStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore(self, **params: Unpack[GoogleTrendsExploreTextResponseParams]) -> str: ...
    @overload
    def trends_explore(self, **params: Unpack[GoogleTrendsExploreDefaultParams]) -> GoogleTrendsExploreResponse: ...
    @overload
    def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionTextResponseParams]) -> str: ...
    @overload
    def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionDefaultParams]) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeTextResponseParams]) -> str: ...
    @overload
    def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeDefaultParams]) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsTextResponseParams]) -> str: ...
    @overload
    def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsDefaultParams]) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesTextResponseParams]) -> str: ...
    @overload
    def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesDefaultParams]) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesTextResponseParams]) -> str: ...
    @overload
    def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesDefaultParams]) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    def trends_locations(self, **params: Unpack[GoogleTrendsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def trends_locations(self, **params: Unpack[GoogleTrendsLocationsTextResponseParams]) -> str: ...
    @overload
    def trends_locations(self, **params: Unpack[GoogleTrendsLocationsDefaultParams]) -> GoogleTrendsLocationsResponse: ...
    @overload
    def trends_trending(self, **params: Unpack[GoogleTrendsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def trends_trending(self, **params: Unpack[GoogleTrendsTrendingTextResponseParams]) -> str: ...
    @overload
    def trends_trending(self, **params: Unpack[GoogleTrendsTrendingDefaultParams]) -> GoogleTrendsTrendingResponse: ...
    @overload
    def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailStreamParams]) -> BinaryIO: ...
    @overload
    def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailTextResponseParams]) -> str: ...
    @overload
    def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailDefaultParams]) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    def videos(self, **params: Unpack[GoogleVideosStreamParams]) -> BinaryIO: ...
    @overload
    def videos(self, **params: Unpack[GoogleVideosTextResponseParams]) -> str: ...
    @overload
    def videos(self, **params: Unpack[GoogleVideosDefaultParams]) -> GoogleVideosResponse: ...

OperationId = Literal[
    'google-finance-analyst-articles',
    'google-finance-chart',
    'google-finance-classification',
    'google-finance-company',
    'google-finance-context',
    'google-finance-financials',
    'google-finance-markets-category-news',
    'google-finance-markets-category-stocks',
    'google-finance-markets-earnings',
    'google-finance-markets-featured',
    'google-finance-markets-headline',
    'google-finance-markets-indices',
    'google-finance-markets-movers',
    'google-finance-markets-top',
    'google-finance-markets-trending',
    'google-finance-news',
    'google-finance-quote',
    'google-finance-related',
    'google-finance-search',
    'google-finance-ticker',
    'google-jobs',
    'google-map-place',
    'google-map-place-photos',
    'google-map-place-reviews',
    'google-map-search',
    'google-news',
    'google-news-search',
    'google-suggest',
    'google-trends-categories',
    'google-trends-enums',
    'google-trends-explore',
    'google-trends-explore-interest-by-region',
    'google-trends-explore-interest-over-time',
    'google-trends-explore-related-topics',
    'google-trends-explore-rising-queries',
    'google-trends-explore-top-queries',
    'google-trends-locations',
    'google-trends-trending',
    'google-trends-trending-detail',
    'google-videos',
]

class CrawloraClient:
    google: GoogleGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-analyst-articles'],
        params: GoogleFinanceAnalystArticlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-chart'],
        params: GoogleFinanceChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceChartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-classification'],
        params: GoogleFinanceClassificationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceClassificationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-company'],
        params: GoogleFinanceCompanyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceCompanyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-context'],
        params: GoogleFinanceContextParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceContextResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-financials'],
        params: GoogleFinanceFinancialsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceFinancialsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-category-news'],
        params: GoogleFinanceMarketsCategoryNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-category-stocks'],
        params: GoogleFinanceMarketsCategoryStocksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-earnings'],
        params: GoogleFinanceMarketsEarningsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-featured'],
        params: GoogleFinanceMarketsFeaturedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-headline'],
        params: GoogleFinanceMarketsHeadlineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-indices'],
        params: GoogleFinanceMarketsIndicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-movers'],
        params: GoogleFinanceMarketsMoversParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-top'],
        params: GoogleFinanceMarketsTopParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-markets-trending'],
        params: GoogleFinanceMarketsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-news'],
        params: GoogleFinanceNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-quote'],
        params: GoogleFinanceQuoteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceQuoteResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-related'],
        params: GoogleFinanceRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-search'],
        params: GoogleFinanceSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-finance-ticker'],
        params: GoogleFinanceTickerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceTickerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-jobs'],
        params: GoogleJobsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleJobsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-map-place'],
        params: GoogleMapPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlaceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-map-place-photos'],
        params: GoogleMapPlacePhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlacePhotosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-map-place-reviews'],
        params: GoogleMapPlaceReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlaceReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-map-search'],
        params: GoogleMapSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-news'],
        params: GoogleNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-news-search'],
        params: GoogleNewsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleNewsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-suggest'],
        params: GoogleSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-categories'],
        params: GoogleTrendsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-enums'],
        params: GoogleTrendsEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsEnumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore'],
        params: GoogleTrendsExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-interest-by-region'],
        params: GoogleTrendsExploreInterestByRegionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-interest-over-time'],
        params: GoogleTrendsExploreInterestOverTimeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-related-topics'],
        params: GoogleTrendsExploreRelatedTopicsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-rising-queries'],
        params: GoogleTrendsExploreRisingQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-explore-top-queries'],
        params: GoogleTrendsExploreTopQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-locations'],
        params: GoogleTrendsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsLocationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-trending'],
        params: GoogleTrendsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-trends-trending-detail'],
        params: GoogleTrendsTrendingDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['google-videos'],
        params: GoogleVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-analyst-articles'],
        params: GoogleFinanceAnalystArticlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-chart'],
        params: GoogleFinanceChartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceChartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-classification'],
        params: GoogleFinanceClassificationParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceClassificationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-company'],
        params: GoogleFinanceCompanyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceCompanyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-context'],
        params: GoogleFinanceContextParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceContextResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-financials'],
        params: GoogleFinanceFinancialsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceFinancialsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-category-news'],
        params: GoogleFinanceMarketsCategoryNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-category-stocks'],
        params: GoogleFinanceMarketsCategoryStocksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-earnings'],
        params: GoogleFinanceMarketsEarningsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-featured'],
        params: GoogleFinanceMarketsFeaturedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-headline'],
        params: GoogleFinanceMarketsHeadlineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-indices'],
        params: GoogleFinanceMarketsIndicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-movers'],
        params: GoogleFinanceMarketsMoversParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-top'],
        params: GoogleFinanceMarketsTopParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-markets-trending'],
        params: GoogleFinanceMarketsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-news'],
        params: GoogleFinanceNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-quote'],
        params: GoogleFinanceQuoteParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceQuoteResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-related'],
        params: GoogleFinanceRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-search'],
        params: GoogleFinanceSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-finance-ticker'],
        params: GoogleFinanceTickerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleFinanceTickerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-jobs'],
        params: GoogleJobsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleJobsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-map-place'],
        params: GoogleMapPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlaceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-map-place-photos'],
        params: GoogleMapPlacePhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlacePhotosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-map-place-reviews'],
        params: GoogleMapPlaceReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapPlaceReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-map-search'],
        params: GoogleMapSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleMapSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-news'],
        params: GoogleNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-news-search'],
        params: GoogleNewsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleNewsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-suggest'],
        params: GoogleSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-categories'],
        params: GoogleTrendsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-enums'],
        params: GoogleTrendsEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsEnumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore'],
        params: GoogleTrendsExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-interest-by-region'],
        params: GoogleTrendsExploreInterestByRegionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-interest-over-time'],
        params: GoogleTrendsExploreInterestOverTimeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-related-topics'],
        params: GoogleTrendsExploreRelatedTopicsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-rising-queries'],
        params: GoogleTrendsExploreRisingQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-explore-top-queries'],
        params: GoogleTrendsExploreTopQueriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-locations'],
        params: GoogleTrendsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsLocationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-trending'],
        params: GoogleTrendsTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-trends-trending-detail'],
        params: GoogleTrendsTrendingDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['google-videos'],
        params: GoogleVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class GoogleClient(CrawloraClient):
    def __enter__(self) -> GoogleClient: ...
    @overload
    def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesTextResponseParams]) -> str: ...
    @overload
    def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesDefaultParams]) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    def finance_chart(self, **params: Unpack[GoogleFinanceChartStreamParams]) -> BinaryIO: ...
    @overload
    def finance_chart(self, **params: Unpack[GoogleFinanceChartTextResponseParams]) -> str: ...
    @overload
    def finance_chart(self, **params: Unpack[GoogleFinanceChartDefaultParams]) -> GoogleFinanceChartResponse: ...
    @overload
    def finance_classification(self, **params: Unpack[GoogleFinanceClassificationStreamParams]) -> BinaryIO: ...
    @overload
    def finance_classification(self, **params: Unpack[GoogleFinanceClassificationTextResponseParams]) -> str: ...
    @overload
    def finance_classification(self, **params: Unpack[GoogleFinanceClassificationDefaultParams]) -> GoogleFinanceClassificationResponse: ...
    @overload
    def finance_company(self, **params: Unpack[GoogleFinanceCompanyStreamParams]) -> BinaryIO: ...
    @overload
    def finance_company(self, **params: Unpack[GoogleFinanceCompanyTextResponseParams]) -> str: ...
    @overload
    def finance_company(self, **params: Unpack[GoogleFinanceCompanyDefaultParams]) -> GoogleFinanceCompanyResponse: ...
    @overload
    def finance_context(self, **params: Unpack[GoogleFinanceContextStreamParams]) -> BinaryIO: ...
    @overload
    def finance_context(self, **params: Unpack[GoogleFinanceContextTextResponseParams]) -> str: ...
    @overload
    def finance_context(self, **params: Unpack[GoogleFinanceContextDefaultParams]) -> GoogleFinanceContextResponse: ...
    @overload
    def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsTextResponseParams]) -> str: ...
    @overload
    def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsDefaultParams]) -> GoogleFinanceFinancialsResponse: ...
    @overload
    def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsTextResponseParams]) -> str: ...
    @overload
    def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsDefaultParams]) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksTextResponseParams]) -> str: ...
    @overload
    def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksDefaultParams]) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsTextResponseParams]) -> str: ...
    @overload
    def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsDefaultParams]) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedTextResponseParams]) -> str: ...
    @overload
    def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedDefaultParams]) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineTextResponseParams]) -> str: ...
    @overload
    def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineDefaultParams]) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesTextResponseParams]) -> str: ...
    @overload
    def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesDefaultParams]) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversTextResponseParams]) -> str: ...
    @overload
    def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversDefaultParams]) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopTextResponseParams]) -> str: ...
    @overload
    def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopDefaultParams]) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingTextResponseParams]) -> str: ...
    @overload
    def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingDefaultParams]) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    def finance_news(self, **params: Unpack[GoogleFinanceNewsStreamParams]) -> BinaryIO: ...
    @overload
    def finance_news(self, **params: Unpack[GoogleFinanceNewsTextResponseParams]) -> str: ...
    @overload
    def finance_news(self, **params: Unpack[GoogleFinanceNewsDefaultParams]) -> GoogleFinanceNewsResponse: ...
    @overload
    def finance_quote(self, **params: Unpack[GoogleFinanceQuoteStreamParams]) -> BinaryIO: ...
    @overload
    def finance_quote(self, **params: Unpack[GoogleFinanceQuoteTextResponseParams]) -> str: ...
    @overload
    def finance_quote(self, **params: Unpack[GoogleFinanceQuoteDefaultParams]) -> GoogleFinanceQuoteResponse: ...
    @overload
    def finance_related(self, **params: Unpack[GoogleFinanceRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def finance_related(self, **params: Unpack[GoogleFinanceRelatedTextResponseParams]) -> str: ...
    @overload
    def finance_related(self, **params: Unpack[GoogleFinanceRelatedDefaultParams]) -> GoogleFinanceRelatedResponse: ...
    @overload
    def finance_search(self, **params: Unpack[GoogleFinanceSearchStreamParams]) -> BinaryIO: ...
    @overload
    def finance_search(self, **params: Unpack[GoogleFinanceSearchTextResponseParams]) -> str: ...
    @overload
    def finance_search(self, **params: Unpack[GoogleFinanceSearchDefaultParams]) -> GoogleFinanceSearchResponse: ...
    @overload
    def finance_ticker(self, **params: Unpack[GoogleFinanceTickerStreamParams]) -> BinaryIO: ...
    @overload
    def finance_ticker(self, **params: Unpack[GoogleFinanceTickerTextResponseParams]) -> str: ...
    @overload
    def finance_ticker(self, **params: Unpack[GoogleFinanceTickerDefaultParams]) -> GoogleFinanceTickerResponse: ...
    @overload
    def jobs(self, **params: Unpack[GoogleJobsStreamParams]) -> BinaryIO: ...
    @overload
    def jobs(self, **params: Unpack[GoogleJobsTextResponseParams]) -> str: ...
    @overload
    def jobs(self, **params: Unpack[GoogleJobsDefaultParams]) -> GoogleJobsResponse: ...
    @overload
    def map_place(self, **params: Unpack[GoogleMapPlaceStreamParams]) -> BinaryIO: ...
    @overload
    def map_place(self, **params: Unpack[GoogleMapPlaceTextResponseParams]) -> str: ...
    @overload
    def map_place(self, **params: Unpack[GoogleMapPlaceDefaultParams]) -> GoogleMapPlaceResponse: ...
    @overload
    def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosTextResponseParams]) -> str: ...
    @overload
    def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosDefaultParams]) -> GoogleMapPlacePhotosResponse: ...
    @overload
    def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsTextResponseParams]) -> str: ...
    @overload
    def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsDefaultParams]) -> GoogleMapPlaceReviewsResponse: ...
    @overload
    def map_search(self, **params: Unpack[GoogleMapSearchStreamParams]) -> BinaryIO: ...
    @overload
    def map_search(self, **params: Unpack[GoogleMapSearchTextResponseParams]) -> str: ...
    @overload
    def map_search(self, **params: Unpack[GoogleMapSearchDefaultParams]) -> GoogleMapSearchResponse: ...
    @overload
    def news(self, **params: Unpack[GoogleNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[GoogleNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[GoogleNewsDefaultParams]) -> GoogleNewsResponse: ...
    @overload
    def news_search(self, **params: Unpack[GoogleNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def news_search(self, **params: Unpack[GoogleNewsSearchTextResponseParams]) -> str: ...
    @overload
    def news_search(self, **params: Unpack[GoogleNewsSearchDefaultParams]) -> GoogleNewsSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[GoogleSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[GoogleSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[GoogleSuggestDefaultParams]) -> GoogleSuggestResponse: ...
    @overload
    def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesTextResponseParams]) -> str: ...
    @overload
    def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesDefaultParams]) -> GoogleTrendsCategoriesResponse: ...
    @overload
    def trends_enums(self, **params: Unpack[GoogleTrendsEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def trends_enums(self, **params: Unpack[GoogleTrendsEnumsTextResponseParams]) -> str: ...
    @overload
    def trends_enums(self, **params: Unpack[GoogleTrendsEnumsDefaultParams]) -> GoogleTrendsEnumsResponse: ...
    @overload
    def trends_explore(self, **params: Unpack[GoogleTrendsExploreStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore(self, **params: Unpack[GoogleTrendsExploreTextResponseParams]) -> str: ...
    @overload
    def trends_explore(self, **params: Unpack[GoogleTrendsExploreDefaultParams]) -> GoogleTrendsExploreResponse: ...
    @overload
    def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionTextResponseParams]) -> str: ...
    @overload
    def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionDefaultParams]) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeTextResponseParams]) -> str: ...
    @overload
    def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeDefaultParams]) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsTextResponseParams]) -> str: ...
    @overload
    def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsDefaultParams]) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesTextResponseParams]) -> str: ...
    @overload
    def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesDefaultParams]) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesStreamParams]) -> BinaryIO: ...
    @overload
    def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesTextResponseParams]) -> str: ...
    @overload
    def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesDefaultParams]) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    def trends_locations(self, **params: Unpack[GoogleTrendsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def trends_locations(self, **params: Unpack[GoogleTrendsLocationsTextResponseParams]) -> str: ...
    @overload
    def trends_locations(self, **params: Unpack[GoogleTrendsLocationsDefaultParams]) -> GoogleTrendsLocationsResponse: ...
    @overload
    def trends_trending(self, **params: Unpack[GoogleTrendsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def trends_trending(self, **params: Unpack[GoogleTrendsTrendingTextResponseParams]) -> str: ...
    @overload
    def trends_trending(self, **params: Unpack[GoogleTrendsTrendingDefaultParams]) -> GoogleTrendsTrendingResponse: ...
    @overload
    def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailStreamParams]) -> BinaryIO: ...
    @overload
    def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailTextResponseParams]) -> str: ...
    @overload
    def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailDefaultParams]) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    def videos(self, **params: Unpack[GoogleVideosStreamParams]) -> BinaryIO: ...
    @overload
    def videos(self, **params: Unpack[GoogleVideosTextResponseParams]) -> str: ...
    @overload
    def videos(self, **params: Unpack[GoogleVideosDefaultParams]) -> GoogleVideosResponse: ...

class AsyncGoogleClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncGoogleClient: ...
    google: _AsyncGoogleGroup
    @overload
    async def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesTextResponseParams]) -> str: ...
    @overload
    async def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesDefaultParams]) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    async def finance_chart(self, **params: Unpack[GoogleFinanceChartStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_chart(self, **params: Unpack[GoogleFinanceChartTextResponseParams]) -> str: ...
    @overload
    async def finance_chart(self, **params: Unpack[GoogleFinanceChartDefaultParams]) -> GoogleFinanceChartResponse: ...
    @overload
    async def finance_classification(self, **params: Unpack[GoogleFinanceClassificationStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_classification(self, **params: Unpack[GoogleFinanceClassificationTextResponseParams]) -> str: ...
    @overload
    async def finance_classification(self, **params: Unpack[GoogleFinanceClassificationDefaultParams]) -> GoogleFinanceClassificationResponse: ...
    @overload
    async def finance_company(self, **params: Unpack[GoogleFinanceCompanyStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_company(self, **params: Unpack[GoogleFinanceCompanyTextResponseParams]) -> str: ...
    @overload
    async def finance_company(self, **params: Unpack[GoogleFinanceCompanyDefaultParams]) -> GoogleFinanceCompanyResponse: ...
    @overload
    async def finance_context(self, **params: Unpack[GoogleFinanceContextStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_context(self, **params: Unpack[GoogleFinanceContextTextResponseParams]) -> str: ...
    @overload
    async def finance_context(self, **params: Unpack[GoogleFinanceContextDefaultParams]) -> GoogleFinanceContextResponse: ...
    @overload
    async def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsTextResponseParams]) -> str: ...
    @overload
    async def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsDefaultParams]) -> GoogleFinanceFinancialsResponse: ...
    @overload
    async def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsDefaultParams]) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    async def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksDefaultParams]) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    async def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsDefaultParams]) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    async def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedDefaultParams]) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    async def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineDefaultParams]) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    async def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesDefaultParams]) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    async def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversDefaultParams]) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    async def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopDefaultParams]) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    async def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingDefaultParams]) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    async def finance_news(self, **params: Unpack[GoogleFinanceNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_news(self, **params: Unpack[GoogleFinanceNewsTextResponseParams]) -> str: ...
    @overload
    async def finance_news(self, **params: Unpack[GoogleFinanceNewsDefaultParams]) -> GoogleFinanceNewsResponse: ...
    @overload
    async def finance_quote(self, **params: Unpack[GoogleFinanceQuoteStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_quote(self, **params: Unpack[GoogleFinanceQuoteTextResponseParams]) -> str: ...
    @overload
    async def finance_quote(self, **params: Unpack[GoogleFinanceQuoteDefaultParams]) -> GoogleFinanceQuoteResponse: ...
    @overload
    async def finance_related(self, **params: Unpack[GoogleFinanceRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_related(self, **params: Unpack[GoogleFinanceRelatedTextResponseParams]) -> str: ...
    @overload
    async def finance_related(self, **params: Unpack[GoogleFinanceRelatedDefaultParams]) -> GoogleFinanceRelatedResponse: ...
    @overload
    async def finance_search(self, **params: Unpack[GoogleFinanceSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_search(self, **params: Unpack[GoogleFinanceSearchTextResponseParams]) -> str: ...
    @overload
    async def finance_search(self, **params: Unpack[GoogleFinanceSearchDefaultParams]) -> GoogleFinanceSearchResponse: ...
    @overload
    async def finance_ticker(self, **params: Unpack[GoogleFinanceTickerStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_ticker(self, **params: Unpack[GoogleFinanceTickerTextResponseParams]) -> str: ...
    @overload
    async def finance_ticker(self, **params: Unpack[GoogleFinanceTickerDefaultParams]) -> GoogleFinanceTickerResponse: ...
    @overload
    async def jobs(self, **params: Unpack[GoogleJobsStreamParams]) -> BinaryIO: ...
    @overload
    async def jobs(self, **params: Unpack[GoogleJobsTextResponseParams]) -> str: ...
    @overload
    async def jobs(self, **params: Unpack[GoogleJobsDefaultParams]) -> GoogleJobsResponse: ...
    @overload
    async def map_place(self, **params: Unpack[GoogleMapPlaceStreamParams]) -> BinaryIO: ...
    @overload
    async def map_place(self, **params: Unpack[GoogleMapPlaceTextResponseParams]) -> str: ...
    @overload
    async def map_place(self, **params: Unpack[GoogleMapPlaceDefaultParams]) -> GoogleMapPlaceResponse: ...
    @overload
    async def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosTextResponseParams]) -> str: ...
    @overload
    async def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosDefaultParams]) -> GoogleMapPlacePhotosResponse: ...
    @overload
    async def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsTextResponseParams]) -> str: ...
    @overload
    async def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsDefaultParams]) -> GoogleMapPlaceReviewsResponse: ...
    @overload
    async def map_search(self, **params: Unpack[GoogleMapSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def map_search(self, **params: Unpack[GoogleMapSearchTextResponseParams]) -> str: ...
    @overload
    async def map_search(self, **params: Unpack[GoogleMapSearchDefaultParams]) -> GoogleMapSearchResponse: ...
    @overload
    async def news(self, **params: Unpack[GoogleNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[GoogleNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[GoogleNewsDefaultParams]) -> GoogleNewsResponse: ...
    @overload
    async def news_search(self, **params: Unpack[GoogleNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def news_search(self, **params: Unpack[GoogleNewsSearchTextResponseParams]) -> str: ...
    @overload
    async def news_search(self, **params: Unpack[GoogleNewsSearchDefaultParams]) -> GoogleNewsSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleSuggestDefaultParams]) -> GoogleSuggestResponse: ...
    @overload
    async def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesDefaultParams]) -> GoogleTrendsCategoriesResponse: ...
    @overload
    async def trends_enums(self, **params: Unpack[GoogleTrendsEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_enums(self, **params: Unpack[GoogleTrendsEnumsTextResponseParams]) -> str: ...
    @overload
    async def trends_enums(self, **params: Unpack[GoogleTrendsEnumsDefaultParams]) -> GoogleTrendsEnumsResponse: ...
    @overload
    async def trends_explore(self, **params: Unpack[GoogleTrendsExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore(self, **params: Unpack[GoogleTrendsExploreTextResponseParams]) -> str: ...
    @overload
    async def trends_explore(self, **params: Unpack[GoogleTrendsExploreDefaultParams]) -> GoogleTrendsExploreResponse: ...
    @overload
    async def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionDefaultParams]) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    async def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeDefaultParams]) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    async def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsDefaultParams]) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    async def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesDefaultParams]) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    async def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesDefaultParams]) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    async def trends_locations(self, **params: Unpack[GoogleTrendsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_locations(self, **params: Unpack[GoogleTrendsLocationsTextResponseParams]) -> str: ...
    @overload
    async def trends_locations(self, **params: Unpack[GoogleTrendsLocationsDefaultParams]) -> GoogleTrendsLocationsResponse: ...
    @overload
    async def trends_trending(self, **params: Unpack[GoogleTrendsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_trending(self, **params: Unpack[GoogleTrendsTrendingTextResponseParams]) -> str: ...
    @overload
    async def trends_trending(self, **params: Unpack[GoogleTrendsTrendingDefaultParams]) -> GoogleTrendsTrendingResponse: ...
    @overload
    async def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailTextResponseParams]) -> str: ...
    @overload
    async def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailDefaultParams]) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    async def videos(self, **params: Unpack[GoogleVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def videos(self, **params: Unpack[GoogleVideosTextResponseParams]) -> str: ...
    @overload
    async def videos(self, **params: Unpack[GoogleVideosDefaultParams]) -> GoogleVideosResponse: ...

class _AsyncGoogleGroup:
    @overload
    async def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesTextResponseParams]) -> str: ...
    @overload
    async def finance_analyst_articles(self, **params: Unpack[GoogleFinanceAnalystArticlesDefaultParams]) -> GoogleFinanceAnalystArticlesResponse: ...
    @overload
    async def finance_chart(self, **params: Unpack[GoogleFinanceChartStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_chart(self, **params: Unpack[GoogleFinanceChartTextResponseParams]) -> str: ...
    @overload
    async def finance_chart(self, **params: Unpack[GoogleFinanceChartDefaultParams]) -> GoogleFinanceChartResponse: ...
    @overload
    async def finance_classification(self, **params: Unpack[GoogleFinanceClassificationStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_classification(self, **params: Unpack[GoogleFinanceClassificationTextResponseParams]) -> str: ...
    @overload
    async def finance_classification(self, **params: Unpack[GoogleFinanceClassificationDefaultParams]) -> GoogleFinanceClassificationResponse: ...
    @overload
    async def finance_company(self, **params: Unpack[GoogleFinanceCompanyStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_company(self, **params: Unpack[GoogleFinanceCompanyTextResponseParams]) -> str: ...
    @overload
    async def finance_company(self, **params: Unpack[GoogleFinanceCompanyDefaultParams]) -> GoogleFinanceCompanyResponse: ...
    @overload
    async def finance_context(self, **params: Unpack[GoogleFinanceContextStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_context(self, **params: Unpack[GoogleFinanceContextTextResponseParams]) -> str: ...
    @overload
    async def finance_context(self, **params: Unpack[GoogleFinanceContextDefaultParams]) -> GoogleFinanceContextResponse: ...
    @overload
    async def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsTextResponseParams]) -> str: ...
    @overload
    async def finance_financials(self, **params: Unpack[GoogleFinanceFinancialsDefaultParams]) -> GoogleFinanceFinancialsResponse: ...
    @overload
    async def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_category_news(self, **params: Unpack[GoogleFinanceMarketsCategoryNewsDefaultParams]) -> GoogleFinanceMarketsCategoryNewsResponse: ...
    @overload
    async def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_category_stocks(self, **params: Unpack[GoogleFinanceMarketsCategoryStocksDefaultParams]) -> GoogleFinanceMarketsCategoryStocksResponse: ...
    @overload
    async def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_earnings(self, **params: Unpack[GoogleFinanceMarketsEarningsDefaultParams]) -> GoogleFinanceMarketsEarningsResponse: ...
    @overload
    async def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_featured(self, **params: Unpack[GoogleFinanceMarketsFeaturedDefaultParams]) -> GoogleFinanceMarketsFeaturedResponse: ...
    @overload
    async def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_headline(self, **params: Unpack[GoogleFinanceMarketsHeadlineDefaultParams]) -> GoogleFinanceMarketsHeadlineResponse: ...
    @overload
    async def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_indices(self, **params: Unpack[GoogleFinanceMarketsIndicesDefaultParams]) -> GoogleFinanceMarketsIndicesResponse: ...
    @overload
    async def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_movers(self, **params: Unpack[GoogleFinanceMarketsMoversDefaultParams]) -> GoogleFinanceMarketsMoversResponse: ...
    @overload
    async def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_top(self, **params: Unpack[GoogleFinanceMarketsTopDefaultParams]) -> GoogleFinanceMarketsTopResponse: ...
    @overload
    async def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingTextResponseParams]) -> str: ...
    @overload
    async def finance_markets_trending(self, **params: Unpack[GoogleFinanceMarketsTrendingDefaultParams]) -> GoogleFinanceMarketsTrendingResponse: ...
    @overload
    async def finance_news(self, **params: Unpack[GoogleFinanceNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_news(self, **params: Unpack[GoogleFinanceNewsTextResponseParams]) -> str: ...
    @overload
    async def finance_news(self, **params: Unpack[GoogleFinanceNewsDefaultParams]) -> GoogleFinanceNewsResponse: ...
    @overload
    async def finance_quote(self, **params: Unpack[GoogleFinanceQuoteStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_quote(self, **params: Unpack[GoogleFinanceQuoteTextResponseParams]) -> str: ...
    @overload
    async def finance_quote(self, **params: Unpack[GoogleFinanceQuoteDefaultParams]) -> GoogleFinanceQuoteResponse: ...
    @overload
    async def finance_related(self, **params: Unpack[GoogleFinanceRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_related(self, **params: Unpack[GoogleFinanceRelatedTextResponseParams]) -> str: ...
    @overload
    async def finance_related(self, **params: Unpack[GoogleFinanceRelatedDefaultParams]) -> GoogleFinanceRelatedResponse: ...
    @overload
    async def finance_search(self, **params: Unpack[GoogleFinanceSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_search(self, **params: Unpack[GoogleFinanceSearchTextResponseParams]) -> str: ...
    @overload
    async def finance_search(self, **params: Unpack[GoogleFinanceSearchDefaultParams]) -> GoogleFinanceSearchResponse: ...
    @overload
    async def finance_ticker(self, **params: Unpack[GoogleFinanceTickerStreamParams]) -> BinaryIO: ...
    @overload
    async def finance_ticker(self, **params: Unpack[GoogleFinanceTickerTextResponseParams]) -> str: ...
    @overload
    async def finance_ticker(self, **params: Unpack[GoogleFinanceTickerDefaultParams]) -> GoogleFinanceTickerResponse: ...
    @overload
    async def jobs(self, **params: Unpack[GoogleJobsStreamParams]) -> BinaryIO: ...
    @overload
    async def jobs(self, **params: Unpack[GoogleJobsTextResponseParams]) -> str: ...
    @overload
    async def jobs(self, **params: Unpack[GoogleJobsDefaultParams]) -> GoogleJobsResponse: ...
    @overload
    async def map_place(self, **params: Unpack[GoogleMapPlaceStreamParams]) -> BinaryIO: ...
    @overload
    async def map_place(self, **params: Unpack[GoogleMapPlaceTextResponseParams]) -> str: ...
    @overload
    async def map_place(self, **params: Unpack[GoogleMapPlaceDefaultParams]) -> GoogleMapPlaceResponse: ...
    @overload
    async def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosTextResponseParams]) -> str: ...
    @overload
    async def map_place_photos(self, **params: Unpack[GoogleMapPlacePhotosDefaultParams]) -> GoogleMapPlacePhotosResponse: ...
    @overload
    async def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsTextResponseParams]) -> str: ...
    @overload
    async def map_place_reviews(self, **params: Unpack[GoogleMapPlaceReviewsDefaultParams]) -> GoogleMapPlaceReviewsResponse: ...
    @overload
    async def map_search(self, **params: Unpack[GoogleMapSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def map_search(self, **params: Unpack[GoogleMapSearchTextResponseParams]) -> str: ...
    @overload
    async def map_search(self, **params: Unpack[GoogleMapSearchDefaultParams]) -> GoogleMapSearchResponse: ...
    @overload
    async def news(self, **params: Unpack[GoogleNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[GoogleNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[GoogleNewsDefaultParams]) -> GoogleNewsResponse: ...
    @overload
    async def news_search(self, **params: Unpack[GoogleNewsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def news_search(self, **params: Unpack[GoogleNewsSearchTextResponseParams]) -> str: ...
    @overload
    async def news_search(self, **params: Unpack[GoogleNewsSearchDefaultParams]) -> GoogleNewsSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleSuggestDefaultParams]) -> GoogleSuggestResponse: ...
    @overload
    async def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def trends_categories(self, **params: Unpack[GoogleTrendsCategoriesDefaultParams]) -> GoogleTrendsCategoriesResponse: ...
    @overload
    async def trends_enums(self, **params: Unpack[GoogleTrendsEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_enums(self, **params: Unpack[GoogleTrendsEnumsTextResponseParams]) -> str: ...
    @overload
    async def trends_enums(self, **params: Unpack[GoogleTrendsEnumsDefaultParams]) -> GoogleTrendsEnumsResponse: ...
    @overload
    async def trends_explore(self, **params: Unpack[GoogleTrendsExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore(self, **params: Unpack[GoogleTrendsExploreTextResponseParams]) -> str: ...
    @overload
    async def trends_explore(self, **params: Unpack[GoogleTrendsExploreDefaultParams]) -> GoogleTrendsExploreResponse: ...
    @overload
    async def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_interest_by_region(self, **params: Unpack[GoogleTrendsExploreInterestByRegionDefaultParams]) -> GoogleTrendsExploreInterestByRegionResponse: ...
    @overload
    async def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_interest_over_time(self, **params: Unpack[GoogleTrendsExploreInterestOverTimeDefaultParams]) -> GoogleTrendsExploreInterestOverTimeResponse: ...
    @overload
    async def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_related_topics(self, **params: Unpack[GoogleTrendsExploreRelatedTopicsDefaultParams]) -> GoogleTrendsExploreRelatedTopicsResponse: ...
    @overload
    async def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_rising_queries(self, **params: Unpack[GoogleTrendsExploreRisingQueriesDefaultParams]) -> GoogleTrendsExploreRisingQueriesResponse: ...
    @overload
    async def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesTextResponseParams]) -> str: ...
    @overload
    async def trends_explore_top_queries(self, **params: Unpack[GoogleTrendsExploreTopQueriesDefaultParams]) -> GoogleTrendsExploreTopQueriesResponse: ...
    @overload
    async def trends_locations(self, **params: Unpack[GoogleTrendsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_locations(self, **params: Unpack[GoogleTrendsLocationsTextResponseParams]) -> str: ...
    @overload
    async def trends_locations(self, **params: Unpack[GoogleTrendsLocationsDefaultParams]) -> GoogleTrendsLocationsResponse: ...
    @overload
    async def trends_trending(self, **params: Unpack[GoogleTrendsTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_trending(self, **params: Unpack[GoogleTrendsTrendingTextResponseParams]) -> str: ...
    @overload
    async def trends_trending(self, **params: Unpack[GoogleTrendsTrendingDefaultParams]) -> GoogleTrendsTrendingResponse: ...
    @overload
    async def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailTextResponseParams]) -> str: ...
    @overload
    async def trends_trending_detail(self, **params: Unpack[GoogleTrendsTrendingDetailDefaultParams]) -> GoogleTrendsTrendingDetailResponse: ...
    @overload
    async def videos(self, **params: Unpack[GoogleVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def videos(self, **params: Unpack[GoogleVideosTextResponseParams]) -> str: ...
    @overload
    async def videos(self, **params: Unpack[GoogleVideosDefaultParams]) -> GoogleVideosResponse: ...

GoogleFinanceAnalystArticlesDefaultParams = TypedDict('GoogleFinanceAnalystArticlesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceAnalystArticlesTextResponseParams = TypedDict('GoogleFinanceAnalystArticlesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceAnalystArticlesStreamParams = TypedDict('GoogleFinanceAnalystArticlesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceChartDefaultParams = TypedDict('GoogleFinanceChartDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceChartTextResponseParams = TypedDict('GoogleFinanceChartTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceChartStreamParams = TypedDict('GoogleFinanceChartStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceClassificationDefaultParams = TypedDict('GoogleFinanceClassificationDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceClassificationTextResponseParams = TypedDict('GoogleFinanceClassificationTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceClassificationStreamParams = TypedDict('GoogleFinanceClassificationStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceCompanyDefaultParams = TypedDict('GoogleFinanceCompanyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceCompanyTextResponseParams = TypedDict('GoogleFinanceCompanyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceCompanyStreamParams = TypedDict('GoogleFinanceCompanyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceContextDefaultParams = TypedDict('GoogleFinanceContextDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
}, total=False)

GoogleFinanceContextTextResponseParams = TypedDict('GoogleFinanceContextTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
}, total=False)

GoogleFinanceContextStreamParams = TypedDict('GoogleFinanceContextStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
}, total=False)

GoogleFinanceFinancialsDefaultParams = TypedDict('GoogleFinanceFinancialsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceFinancialsTextResponseParams = TypedDict('GoogleFinanceFinancialsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceFinancialsStreamParams = TypedDict('GoogleFinanceFinancialsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceMarketsCategoryNewsDefaultParams = TypedDict('GoogleFinanceMarketsCategoryNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryNewsTextResponseParams = TypedDict('GoogleFinanceMarketsCategoryNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryNewsStreamParams = TypedDict('GoogleFinanceMarketsCategoryNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryStocksDefaultParams = TypedDict('GoogleFinanceMarketsCategoryStocksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryStocksTextResponseParams = TypedDict('GoogleFinanceMarketsCategoryStocksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsCategoryStocksStreamParams = TypedDict('GoogleFinanceMarketsCategoryStocksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': Required[str],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsEarningsDefaultParams = TypedDict('GoogleFinanceMarketsEarningsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GoogleFinanceMarketsEarningsTextResponseParams = TypedDict('GoogleFinanceMarketsEarningsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GoogleFinanceMarketsEarningsStreamParams = TypedDict('GoogleFinanceMarketsEarningsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GoogleFinanceMarketsFeaturedDefaultParams = TypedDict('GoogleFinanceMarketsFeaturedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GoogleFinanceMarketsFeaturedTextResponseParams = TypedDict('GoogleFinanceMarketsFeaturedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GoogleFinanceMarketsFeaturedStreamParams = TypedDict('GoogleFinanceMarketsFeaturedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GoogleFinanceMarketsHeadlineDefaultParams = TypedDict('GoogleFinanceMarketsHeadlineDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GoogleFinanceMarketsHeadlineTextResponseParams = TypedDict('GoogleFinanceMarketsHeadlineTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GoogleFinanceMarketsHeadlineStreamParams = TypedDict('GoogleFinanceMarketsHeadlineStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GoogleFinanceMarketsIndicesDefaultParams = TypedDict('GoogleFinanceMarketsIndicesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GoogleFinanceMarketsIndicesTextResponseParams = TypedDict('GoogleFinanceMarketsIndicesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GoogleFinanceMarketsIndicesStreamParams = TypedDict('GoogleFinanceMarketsIndicesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GoogleFinanceMarketsMoversDefaultParams = TypedDict('GoogleFinanceMarketsMoversDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'categories': NotRequired[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsMoversTextResponseParams = TypedDict('GoogleFinanceMarketsMoversTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'categories': NotRequired[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsMoversStreamParams = TypedDict('GoogleFinanceMarketsMoversStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'categories': NotRequired[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTopDefaultParams = TypedDict('GoogleFinanceMarketsTopDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTopTextResponseParams = TypedDict('GoogleFinanceMarketsTopTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTopStreamParams = TypedDict('GoogleFinanceMarketsTopStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'metric': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTrendingDefaultParams = TypedDict('GoogleFinanceMarketsTrendingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTrendingTextResponseParams = TypedDict('GoogleFinanceMarketsTrendingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceMarketsTrendingStreamParams = TypedDict('GoogleFinanceMarketsTrendingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceNewsDefaultParams = TypedDict('GoogleFinanceNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceNewsTextResponseParams = TypedDict('GoogleFinanceNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceNewsStreamParams = TypedDict('GoogleFinanceNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleFinanceQuoteDefaultParams = TypedDict('GoogleFinanceQuoteDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceQuoteTextResponseParams = TypedDict('GoogleFinanceQuoteTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceQuoteStreamParams = TypedDict('GoogleFinanceQuoteStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceRelatedDefaultParams = TypedDict('GoogleFinanceRelatedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceRelatedTextResponseParams = TypedDict('GoogleFinanceRelatedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceRelatedStreamParams = TypedDict('GoogleFinanceRelatedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'quote': Required[str],
}, total=False)

GoogleFinanceSearchDefaultParams = TypedDict('GoogleFinanceSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
}, total=False)

GoogleFinanceSearchTextResponseParams = TypedDict('GoogleFinanceSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
}, total=False)

GoogleFinanceSearchStreamParams = TypedDict('GoogleFinanceSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
}, total=False)

GoogleFinanceTickerDefaultParams = TypedDict('GoogleFinanceTickerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ticker': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceTickerTextResponseParams = TypedDict('GoogleFinanceTickerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ticker': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleFinanceTickerStreamParams = TypedDict('GoogleFinanceTickerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ticker': Required[str],
    'window': NotRequired[str],
}, total=False)

GoogleJobsDefaultParams = TypedDict('GoogleJobsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'option': Required[GoogleJobsBody],
}, total=False)

GoogleJobsTextResponseParams = TypedDict('GoogleJobsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'option': Required[GoogleJobsBody],
}, total=False)

GoogleJobsStreamParams = TypedDict('GoogleJobsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'option': Required[GoogleJobsBody],
}, total=False)

GoogleMapPlaceDefaultParams = TypedDict('GoogleMapPlaceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'place_id': Required[str],
}, total=False)

GoogleMapPlaceTextResponseParams = TypedDict('GoogleMapPlaceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'place_id': Required[str],
}, total=False)

GoogleMapPlaceStreamParams = TypedDict('GoogleMapPlaceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'place_id': Required[str],
}, total=False)

GoogleMapPlacePhotosDefaultParams = TypedDict('GoogleMapPlacePhotosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapPlacePhotosTextResponseParams = TypedDict('GoogleMapPlacePhotosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapPlacePhotosStreamParams = TypedDict('GoogleMapPlacePhotosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapPlaceReviewsDefaultParams = TypedDict('GoogleMapPlaceReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapPlaceReviewsTextResponseParams = TypedDict('GoogleMapPlaceReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapPlaceReviewsStreamParams = TypedDict('GoogleMapPlaceReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'place_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

GoogleMapSearchDefaultParams = TypedDict('GoogleMapSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'mapSearchOption': Required[GoogleMapSearchBody],
}, total=False)

GoogleMapSearchTextResponseParams = TypedDict('GoogleMapSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'mapSearchOption': Required[GoogleMapSearchBody],
}, total=False)

GoogleMapSearchStreamParams = TypedDict('GoogleMapSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'mapSearchOption': Required[GoogleMapSearchBody],
}, total=False)

GoogleNewsDefaultParams = TypedDict('GoogleNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleNewsTextResponseParams = TypedDict('GoogleNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleNewsStreamParams = TypedDict('GoogleNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleNewsSearchDefaultParams = TypedDict('GoogleNewsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'searchOption': Required[GoogleNewsSearchBody],
}, total=False)

GoogleNewsSearchTextResponseParams = TypedDict('GoogleNewsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'searchOption': Required[GoogleNewsSearchBody],
}, total=False)

GoogleNewsSearchStreamParams = TypedDict('GoogleNewsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'searchOption': Required[GoogleNewsSearchBody],
}, total=False)

GoogleSuggestDefaultParams = TypedDict('GoogleSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'source': NotRequired[Literal['web', 'youtube', 'shopping']],
    'rich': NotRequired[bool],
}, total=False)

GoogleSuggestTextResponseParams = TypedDict('GoogleSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'source': NotRequired[Literal['web', 'youtube', 'shopping']],
    'rich': NotRequired[bool],
}, total=False)

GoogleSuggestStreamParams = TypedDict('GoogleSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'source': NotRequired[Literal['web', 'youtube', 'shopping']],
    'rich': NotRequired[bool],
}, total=False)

GoogleTrendsCategoriesDefaultParams = TypedDict('GoogleTrendsCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GoogleTrendsCategoriesTextResponseParams = TypedDict('GoogleTrendsCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GoogleTrendsCategoriesStreamParams = TypedDict('GoogleTrendsCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GoogleTrendsEnumsDefaultParams = TypedDict('GoogleTrendsEnumsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GoogleTrendsEnumsTextResponseParams = TypedDict('GoogleTrendsEnumsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GoogleTrendsEnumsStreamParams = TypedDict('GoogleTrendsEnumsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GoogleTrendsExploreDefaultParams = TypedDict('GoogleTrendsExploreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'request': Required[GoogleTrendsExploreBody],
}, total=False)

GoogleTrendsExploreTextResponseParams = TypedDict('GoogleTrendsExploreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'request': Required[GoogleTrendsExploreBody],
}, total=False)

GoogleTrendsExploreStreamParams = TypedDict('GoogleTrendsExploreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'request': Required[GoogleTrendsExploreBody],
}, total=False)

GoogleTrendsExploreInterestByRegionDefaultParams = TypedDict('GoogleTrendsExploreInterestByRegionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'request': Required[GoogleTrendsExploreInterestByRegionBody],
}, total=False)

GoogleTrendsExploreInterestByRegionTextResponseParams = TypedDict('GoogleTrendsExploreInterestByRegionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'request': Required[GoogleTrendsExploreInterestByRegionBody],
}, total=False)

GoogleTrendsExploreInterestByRegionStreamParams = TypedDict('GoogleTrendsExploreInterestByRegionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'request': Required[GoogleTrendsExploreInterestByRegionBody],
}, total=False)

GoogleTrendsExploreInterestOverTimeDefaultParams = TypedDict('GoogleTrendsExploreInterestOverTimeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'request': Required[GoogleTrendsExploreInterestOverTimeBody],
}, total=False)

GoogleTrendsExploreInterestOverTimeTextResponseParams = TypedDict('GoogleTrendsExploreInterestOverTimeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'request': Required[GoogleTrendsExploreInterestOverTimeBody],
}, total=False)

GoogleTrendsExploreInterestOverTimeStreamParams = TypedDict('GoogleTrendsExploreInterestOverTimeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'request': Required[GoogleTrendsExploreInterestOverTimeBody],
}, total=False)

GoogleTrendsExploreRelatedTopicsDefaultParams = TypedDict('GoogleTrendsExploreRelatedTopicsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'request': Required[GoogleTrendsExploreRelatedTopicsBody],
}, total=False)

GoogleTrendsExploreRelatedTopicsTextResponseParams = TypedDict('GoogleTrendsExploreRelatedTopicsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'request': Required[GoogleTrendsExploreRelatedTopicsBody],
}, total=False)

GoogleTrendsExploreRelatedTopicsStreamParams = TypedDict('GoogleTrendsExploreRelatedTopicsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'request': Required[GoogleTrendsExploreRelatedTopicsBody],
}, total=False)

GoogleTrendsExploreRisingQueriesDefaultParams = TypedDict('GoogleTrendsExploreRisingQueriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'request': Required[GoogleTrendsExploreRisingQueriesBody],
}, total=False)

GoogleTrendsExploreRisingQueriesTextResponseParams = TypedDict('GoogleTrendsExploreRisingQueriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'request': Required[GoogleTrendsExploreRisingQueriesBody],
}, total=False)

GoogleTrendsExploreRisingQueriesStreamParams = TypedDict('GoogleTrendsExploreRisingQueriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'request': Required[GoogleTrendsExploreRisingQueriesBody],
}, total=False)

GoogleTrendsExploreTopQueriesDefaultParams = TypedDict('GoogleTrendsExploreTopQueriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'request': Required[GoogleTrendsExploreTopQueriesBody],
}, total=False)

GoogleTrendsExploreTopQueriesTextResponseParams = TypedDict('GoogleTrendsExploreTopQueriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'request': Required[GoogleTrendsExploreTopQueriesBody],
}, total=False)

GoogleTrendsExploreTopQueriesStreamParams = TypedDict('GoogleTrendsExploreTopQueriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'request': Required[GoogleTrendsExploreTopQueriesBody],
}, total=False)

GoogleTrendsLocationsDefaultParams = TypedDict('GoogleTrendsLocationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GoogleTrendsLocationsTextResponseParams = TypedDict('GoogleTrendsLocationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GoogleTrendsLocationsStreamParams = TypedDict('GoogleTrendsLocationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GoogleTrendsTrendingDefaultParams = TypedDict('GoogleTrendsTrendingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'geo': NotRequired[Literal['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'tz': NotRequired[int],
    'window': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'time_range': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'category': NotRequired[Literal['0', '3', '47', '44', '22', '12', '5', '7', '71', '8', '45', '65', '11', '13', '958', '19', '16', '299', '14', '66', '29', '533', '174', '18', '20', '67']],
    'status': NotRequired[Literal['all', 'active', 'ended']],
    'sort_by': NotRequired[Literal['relevance', 'title', 'recency', 'search_volume']],
    'limit': NotRequired[int],
}, total=False)

GoogleTrendsTrendingTextResponseParams = TypedDict('GoogleTrendsTrendingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'geo': NotRequired[Literal['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'tz': NotRequired[int],
    'window': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'time_range': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'category': NotRequired[Literal['0', '3', '47', '44', '22', '12', '5', '7', '71', '8', '45', '65', '11', '13', '958', '19', '16', '299', '14', '66', '29', '533', '174', '18', '20', '67']],
    'status': NotRequired[Literal['all', 'active', 'ended']],
    'sort_by': NotRequired[Literal['relevance', 'title', 'recency', 'search_volume']],
    'limit': NotRequired[int],
}, total=False)

GoogleTrendsTrendingStreamParams = TypedDict('GoogleTrendsTrendingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'geo': NotRequired[Literal['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'VG', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'BQ', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'XK', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'KP', 'MK', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'KR', 'SS', 'ES', 'LK', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'SD', 'SR', 'SJ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'VI', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'WF', 'EH', 'YE', 'ZM', 'ZW']],
    'hl': NotRequired[str],
    'tz': NotRequired[int],
    'window': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'time_range': NotRequired[Literal['4h', '24h', '48h', '7d']],
    'category': NotRequired[Literal['0', '3', '47', '44', '22', '12', '5', '7', '71', '8', '45', '65', '11', '13', '958', '19', '16', '299', '14', '66', '29', '533', '174', '18', '20', '67']],
    'status': NotRequired[Literal['all', 'active', 'ended']],
    'sort_by': NotRequired[Literal['relevance', 'title', 'recency', 'search_volume']],
    'limit': NotRequired[int],
}, total=False)

GoogleTrendsTrendingDetailDefaultParams = TypedDict('GoogleTrendsTrendingDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'request': Required[GoogleTrendsTrendingDetailBody],
}, total=False)

GoogleTrendsTrendingDetailTextResponseParams = TypedDict('GoogleTrendsTrendingDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'request': Required[GoogleTrendsTrendingDetailBody],
}, total=False)

GoogleTrendsTrendingDetailStreamParams = TypedDict('GoogleTrendsTrendingDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'request': Required[GoogleTrendsTrendingDetailBody],
}, total=False)

GoogleVideosDefaultParams = TypedDict('GoogleVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleVideosTextResponseParams = TypedDict('GoogleVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleVideosStreamParams = TypedDict('GoogleVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

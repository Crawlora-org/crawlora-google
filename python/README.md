# crawlora-google — Google API client for Python

Python client for Crawlora's hosted Google API. It exposes 40 API endpoints covering Maps search, places, reviews and photos; News; Trends; Finance quotes and markets; suggestions; videos; and jobs. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-python-homepage); the package does not run a browser or scrape
Google locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Google or its owners.

## Install

```sh
python -m pip install crawlora-google
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=google-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_google import GoogleClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with GoogleClient(api_key=api_key) as client:
    result_1 = client.news(q='artificial intelligence')
    print(result_1)
    result_2 = client.map_search(mapSearchOption={'keyword': 'coffee shops in Seattle', 'country': 'us', 'language': 'en'})
    print(result_2)
    result_3 = client.trends_trending(geo='US')
    print(result_3)
```

The package also exports `Client` as an alias for `GoogleClient`. Operation
methods are available directly in snake_case and through the `google`
group. The async package client is `AsyncGoogleClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-google/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-google/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_google import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.news(q='artificial intelligence')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-google/blob/main/examples/python.py) for a complete usage example.

## Supported Google API endpoints

This package exposes every route below through direct snake_case methods and the `google` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-google/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.

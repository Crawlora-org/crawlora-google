import os

from crawlora_google import GoogleClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with GoogleClient(api_key=api_key) as client:
    news = client.news(q='artificial intelligence')
    print('news', news)
    map_search = client.map_search(mapSearchOption={'keyword': 'coffee shops in Seattle', 'country': 'us', 'language': 'en'})
    print('map_search', map_search)
    trends_trending = client.trends_trending(geo='US')
    print('trends_trending', trends_trending)

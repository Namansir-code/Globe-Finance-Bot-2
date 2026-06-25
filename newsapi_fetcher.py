import requests
from config import NEWS_API_KEY

def get_newsapi_news():

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=stock market OR IPO OR finance&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"apiKey={NEWS_API_KEY}"
    )

    r = requests.get(url)

    data = r.json()

    articles = []

    for item in data.get("articles", [])[:5]:
        articles.append({
            "title": item["title"],
            "link": item["url"]
        })

    return articles

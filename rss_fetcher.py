import feedparser

RSS_FEEDS = [
    "https://feeds.feedburner.com/ndtvprofit-latest",
]

def get_rss_news():
    news = []

    for feed in RSS_FEEDS:
        parsed = feedparser.parse(feed)

        for item in parsed.entries[:5]:
            news.append({
                "title": item.title,
                "link": item.link
            })

    return news

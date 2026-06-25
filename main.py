import json
import os

from rss_fetcher import get_rss_news
from newsapi_fetcher import get_newsapi_news
from gemini_summarizer import summarize_news
from telegram_sender import send_message

SEEN_FILE = "seen_news.json"


def load_seen():

    if not os.path.exists(SEEN_FILE):
        return []

    with open(SEEN_FILE, "r") as f:
        return json.load(f)


def save_seen(data):

    with open(SEEN_FILE, "w") as f:
        json.dump(data, f)


def run():

    seen = load_seen()

    news = []

    news.extend(get_rss_news())
    news.extend(get_newsapi_news())

    for item in news:

        title = item["title"]

        if title in seen:
            continue

        try:

            summary = summarize_news(title)

            post = (
                f"{summary}\n\n"
                f"🔗 {item['link']}"
            )

            send_message(post)

            seen.append(title)

        except Exception as e:
            print(e)

    save_seen(seen)


if __name__ == "__main__":
    run()

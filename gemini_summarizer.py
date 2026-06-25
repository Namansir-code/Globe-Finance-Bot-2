import requests
from config import GEMINI_API_KEY

def summarize_news(headline):

    prompt = f"""
Convert this finance headline into a short Telegram post.

Headline:
{headline}

Format:

🚨 Finance Update

What happened?
Why it matters?
Investor takeaway?

Keep under 80 words.
"""

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    r = requests.post(url, json=payload)

    data = r.json()

    return data["candidates"][0]["content"]["parts"][0]["text"]

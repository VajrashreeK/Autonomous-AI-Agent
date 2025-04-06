import requests
from bs4 import BeautifulSoup

def fetch_news(topic, limit):
    url = f"https://news.google.com/search?q={topic}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h.text for h in soup.select('article h3')][:limit]
    return headlines

def fetch_reviews(product):
    return [
        {"pros": ["Good battery", "Nice camera"], "cons": ["Expensive"]},
        {"pros": ["Smooth UI"], "cons": ["Low storage"]},
    ]

def fetch_data(topic):
    return [
        {"year": 2021, "value": 100},
        {"year": 2022, "value": 130},
    ]

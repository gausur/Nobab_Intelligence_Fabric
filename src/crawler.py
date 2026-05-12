import time
import requests
from bs4 import BeautifulSoup

def crawl_page(url, depth=1):
    if depth <= 0:
        return []
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return []
        soup = BeautifulSoup(resp.text, "lxml")
        text = soup.get_text(separator=" ", strip=True)[:3000]
        data = [{"url": url, "text": text, "timestamp": time.time()}]
        return data
    except:
        return []

if __name__ == "__main__":
    print(crawl_page("https://example.com"))

import re
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from config import SEARCH_ENGINES, AHMIA_ENABLED, TOR_PROXY

session = requests.Session()
if TOR_PROXY:
    session.proxies = {"http": TOR_PROXY, "https": TOR_PROXY}

def extract_links(html, base_url):
    """BeautifulSoup ব্যবহার করে HTML থেকে সব লিংক বের করে"""
    soup = BeautifulSoup(html, "lxml")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith("http"):
            links.append(href)
        elif href.startswith("/") and not href.startswith("//"):
            from urllib.parse import urljoin
            links.append(urljoin(base_url, href))
    return links

def search_web(keyword):
    """Google/Bing/Ahmia সার্চ করে ইউআরএল আবিষ্কার"""
    urls = []
    for engine, base in SEARCH_ENGINES.items():
        if engine == "ahmia" and not AHMIA_ENABLED:
            continue
        try:
            resp = session.get(base + quote_plus(keyword), timeout=15)
            if resp.status_code != 200:
                continue
            new_links = extract_links(resp.text, base)
            urls.extend(new_links)
        except Exception as e:
            print(f"Search error for {engine}: {e}")
    # Basic filtering
    filtered = []
    for u in set(urls):
        if any(skip in u for skip in ["google.", "youtube.", "facebook.", "twitter."]):
            continue
        filtered.append(u)
    return filtered[:50]

if __name__ == "__main__":
    # টেস্ট রান
    test_keyword = "ransomware attack"
    found = search_web(test_keyword)
    print(f"Found {len(found)} links for {test_keyword}")

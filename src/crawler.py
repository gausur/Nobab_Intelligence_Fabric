import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from config import TOR_PROXY

session = requests.Session()
if TOR_PROXY:
    session.proxies = {"http": TOR_PROXY, "https": TOR_PROXY}

def is_same_domain(url, base_domain):
    """লিংক একই ডোমেইনের কিনা চেক করে"""
    parsed = urlparse(url)
    return parsed.netloc == base_domain

def crawl_page(url, depth=2, visited=None, domain=None):
    """রিকার্সিভ ক্রলিং - টেক্সট ও লিংক সংগ্রহ"""
    if visited is None:
        visited = set()
    if url in visited or depth <= 0:
        return []

    visited.add(url)
    try:
        resp = session.get(url, timeout=10)
        if resp.status_code != 200:
            return []
        soup = BeautifulSoup(resp.text, "lxml")
        text = soup.get_text(separator=" ", strip=True)

        # লিংক বের করা
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            full_url = urljoin(url, href)
            if domain is None:
                links.append(full_url)
            elif is_same_domain(full_url, domain):
                links.append(full_url)

        data = [{"url": url, "text": text, "timestamp": time.time()}]

        # রিকার্সিভ কল - শুধু প্রথম ১০টি লিংক অনুসরণ করে
        for link in links[:10]:
            data.extend(crawl_page(link, depth-1, visited, domain))
        return data
    except Exception as e:
        print(f"Crawl error {url}: {e}")
        return []

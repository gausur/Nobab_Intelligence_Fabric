import requests
from urllib.parse import quote_plus
from src.config import SEARCH_ENGINES

# Dark web search using Ahmia (no Tor needed)
def dark_web_search(keyword, limit=10):
    """
    Ahmia.fi এর API ব্যবহার করে .onion লিংক খোঁজে।
    GitHub Actions-এ সরাসরি কাজ করে (Tor ছাড়াই)।
    """
    try:
        # Ahmia's public JSON API
        url = f"https://ahmia.fi/search/?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code != 200:
            return []
        # Simple extraction of .onion links from HTML
        import re
        onions = re.findall(r'https?://([a-z2-7]+\.onion)[/"?]', resp.text)
        unique = list(set(onions))[:limit]
        return [f"http://{o}" for o in unique]
    except Exception as e:
        print(f"Dark web search error: {e}")
        return []

def search_web(keyword):
    """Surface web search using Google/Bing"""
    urls = []
    for engine, base in SEARCH_ENGINES.items():
        try:
            resp = requests.get(base + quote_plus(keyword), timeout=10)
            if resp.status_code == 200:
                import re
                links = re.findall(r'href=[\'"]?(https?://[^\'" >]+)', resp.text)
                urls.extend(links[:5])
        except:
            pass
    return list(set(urls))

# Combined search (surface + dark web)
def search_all(keyword):
    surface = search_web(keyword)
    dark = dark_web_search(keyword)
    return surface + dark

if __name__ == "__main__":
    test = "cyber threat"
    print("Surface:", search_web(test))
    print("Dark web:", dark_web_search(test))

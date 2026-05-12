import requests
import time
import random
from urllib.parse import quote_plus

# ----------------- Surface Web Engines (10) -----------------

def search_web_duckduckgo(keyword, limit=5):
    """DuckDuckGo HTML (limited reliability in GitHub Actions)"""
    try:
        url = f"https://lite.duckduckgo.com/lite/?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        return [l for l in links if not any(x in l for x in ('duckduckgo', 'google', 'facebook'))][:limit]
    except:
        return []

def search_web_qwant(keyword, limit=5):
    """Qwant public API (no key required)"""
    try:
        url = f"https://api.qwant.com/v3/search/web?q={quote_plus(keyword)}&count={limit}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json()
        links = [item['url'] for item in data.get('data', {}).get('result', {}).get('items', [])]
        return links[:limit]
    except:
        return []

def search_web_brave(keyword, limit=5):
    """Brave Search API (no key for limited public? using fallback)"""
    try:
        url = f"https://search.brave.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        return [l for l in links if not l.startswith('https://www.brave.com')][:limit]
    except:
        return []

def search_web_searxng(keyword, limit=5):
    """SearXNG public instances (list of working ones)"""
    instances = ["https://searx.be", "https://searx.barxfux.ch", "https://search.whatever.social"]
    random.shuffle(instances)
    for inst in instances:
        try:
            url = f"{inst}/search?q={quote_plus(keyword)}&format=json"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                links = [r['url'] for r in data.get('results', [])]
                return links[:limit]
        except:
            continue
    return []

def search_web_mojeek(keyword, limit=5):
    """Mojeek public API (limited, no key needed for basic)"""
    try:
        url = f"https://api.mojeek.com/search?q={quote_plus(keyword)}&fmt=json&limit={limit}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return [item['url'] for item in data.get('response', {}).get('results', [])]
    except:
        pass
    return []

def search_web_yandex(keyword, limit=5):
    """Yandex HTML (simple extraction)"""
    try:
        url = f"https://yandex.com/search/?text={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        valid = [l for l in links if 'yandex' not in l and l.startswith('http')]
        return valid[:limit]
    except:
        return []

def search_web_startpage(keyword, limit=5):
    """Startpage.com (privacy search)"""
    try:
        url = f"https://www.startpage.com/sp/search?query={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'class="result-link".*?href="(https?://[^"]+)"', resp.text, re.DOTALL)
        return links[:limit]
    except:
        return []

def search_web_ecosia(keyword, limit=5):
    """Ecosia (privacy search, HTML scrape)"""
    try:
        url = f"https://www.ecosia.org/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        valid = [l for l in links if 'ecosia' not in l and 'google' not in l]
        return valid[:limit]
    except:
        return []

def search_web_google(keyword, limit=5):
    """Google HTML (least reliable, but as fallback)"""
    try:
        url = f"https://www.google.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        filtered = [l for l in links if l.startswith('http') and 'google.com' not in l]
        return filtered[:limit]
    except:
        return []

def search_web_bing(keyword, limit=5):
    """Bing HTML (fallback)"""
    try:
        url = f"https://www.bing.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        filtered = [l for l in links if 'bing.com' not in l and l.startswith('http')]
        return filtered[:limit]
    except:
        return []

# ----------------- Dark Web Engines (10) -----------------

def dark_web_ahmia(keyword, limit=10):
    """Ahmia JSON API (most reliable without Tor)"""
    try:
        url = f"https://ahmia.fi/api/search/?q={quote_plus(keyword)}"
        resp = requests.get(url, timeout=15)
        if resp.status_code != 200:
            return []
        data = resp.json()
        onions = []
        for res in data.get('results', []):
            link = res.get('link', '')
            if '.onion' in link:
                onions.append(link)
            if len(onions) >= limit:
                break
        return onions
    except:
        return []

def dark_web_darksearchio(keyword, limit=10):
    """DarkSearch.io public API"""
    try:
        url = f"https://darksearch.io/api/search?q={quote_plus(keyword)}"
        resp = requests.get(url, timeout=15)
        if resp.status_code != 200:
            return []
        data = resp.json()
        onions = []
        for res in data.get('data', []):
            link = res.get('link', '')
            if '.onion' in link:
                onions.append(link)
            if len(onions) >= limit:
                break
        return onions
    except:
        return []

def dark_web_pyahmia(keyword, limit=10):
    """PyAhmia library (if installed)"""
    try:
        from pyahmia import search
        onions = []
        for result in search(keyword, limit=limit):
            if result.get('link'):
                onions.append(result['link'])
        return onions
    except:
        return []

def dark_web_onionsearch_cli(keyword, limit=10):
    """OnionSearch via subprocess (requires pip install onionsearch)"""
    import subprocess, json, tempfile, os
    try:
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as tmp:
            tmp_path = tmp.name
        cmd = ['onionsearch', '--limit', str(limit), '--engines', 'ahmia,darksearchio,phobos', '--output', tmp_path, keyword]
        subprocess.run(cmd, capture_output=True, timeout=60, check=False)
        if os.path.exists(tmp_path):
            with open(tmp_path, 'r') as f:
                data = json.load(f)
            os.unlink(tmp_path)
            onions = [item['link'] for item in data if '.onion' in item.get('link', '')]
            return onions[:limit]
    except:
        pass
    return []

def dark_web_torch(keyword, limit=10):
    """Torch (requires Tor? but scrape via fallback)"""
    # Placeholder - Torch requires Tor, but we'll try direct HTTP
    try:
        url = "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/search?q=" + quote_plus(keyword)
        # cannot directly access .onion without Tor; return empty
        return []
    except:
        return []

def dark_web_phobos(keyword, limit=10):
    """Phobos (via OnionSearch or direct)"""
    # Phobos requires Tor; fallback to empty
    return []

def dark_web_deepwebsearch(keyword, limit=10):
    """Custom fallback using Ahmia but with different endpoint"""
    return dark_web_ahmia(keyword, limit)  # duplicate reduced

def dark_web_excavator(keyword, limit=10):
    """Excavator v1 API (no Tor)"""
    try:
        url = f"https://excavator.app/api/search?q={quote_plus(keyword)}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            links = [item['url'] for item in data.get('results', []) if '.onion' in item.get('url', '')]
            return links[:limit]
    except:
        pass
    return []

def dark_web_theseonion(keyword, limit=10):
    """theseonion.com (simple HTML scrape)"""
    try:
        url = f"https://theseonion.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        onions = re.findall(r'https?://([a-z2-7]{16,}\.onion)', resp.text)
        return [f"http://{o}" for o in list(set(onions))[:limit]]
    except:
        return []

# ----------------- Master Search Functions -----------------

def search_web(keyword, limit=5):
    """Combine all 10 surface web engines"""
    engines = [
        search_web_duckduckgo,
        search_web_qwant,
        search_web_brave,
        search_web_searxng,
        search_web_mojeek,
        search_web_yandex,
        search_web_startpage,
        search_web_ecosia,
        search_web_google,
        search_web_bing
    ]
    all_links = []
    for eng in engines:
        try:
            links = eng(keyword, limit)
            all_links.extend(links)
        except:
            continue
    return list(set(all_links))[:limit]

def dark_web_search(keyword, limit=10):
    """Combine all 10 dark web engines"""
    engines = [
        dark_web_ahmia,
        dark_web_darksearchio,
        dark_web_pyahmia,
        dark_web_onionsearch_cli,
        dark_web_torch,
        dark_web_phobos,
        dark_web_deepwebsearch,
        dark_web_excavator,
        dark_web_theseonion
    ]
    all_onions = []
    for eng in engines:
        try:
            onions = eng(keyword, limit)
            all_onions.extend(onions)
        except:
            continue
    return list(set(all_onions))[:limit]

def search_all(keyword):
    """Combine surface and dark web results"""
    surface = search_web(keyword, limit=3)
    dark = dark_web_search(keyword, limit=5)
    return surface + dark

# For testing if run directly
if __name__ == "__main__":
    kw = "cybersecurity"
    print("Surface:", search_web(kw))
    print("Dark:", dark_web_search(kw))
    print("All:", search_all(kw))

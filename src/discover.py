import requests
import time
import random
from urllib.parse import quote_plus

# ------------------------------------------------------------
# Surface Web Engines (10)
# ------------------------------------------------------------

def search_surface_duckduckgo(keyword, limit=5):
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

def search_surface_qwant(keyword, limit=5):
    try:
        url = f"https://api.qwant.com/v3/search/web?q={quote_plus(keyword)}&count={limit}"
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json()
        return [item['url'] for item in data.get('data', {}).get('result', {}).get('items', [])][:limit]
    except:
        return []

def search_surface_brave(keyword, limit=5):
    try:
        url = f"https://search.brave.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        return [l for l in links if 'brave.com' not in l and l.startswith('http')][:limit]
    except:
        return []

def search_surface_searxng(keyword, limit=5):
    instances = ["https://searx.be", "https://searx.barxfux.ch", "https://search.whatever.social"]
    random.shuffle(instances)
    for inst in instances:
        try:
            url = f"{inst}/search?q={quote_plus(keyword)}&format=json"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                return [r['url'] for r in data.get('results', [])][:limit]
        except:
            continue
    return []

def search_surface_mojeek(keyword, limit=5):
    try:
        url = f"https://api.mojeek.com/search?q={quote_plus(keyword)}&fmt=json&limit={limit}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return [item['url'] for item in data.get('response', {}).get('results', [])][:limit]
    except:
        pass
    return []

def search_surface_yandex(keyword, limit=5):
    try:
        url = f"https://yandex.com/search/?text={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        return [l for l in links if 'yandex' not in l and l.startswith('http')][:limit]
    except:
        return []

def search_surface_startpage(keyword, limit=5):
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

def search_surface_ecosia(keyword, limit=5):
    try:
        url = f"https://www.ecosia.org/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        return [l for l in links if 'ecosia' not in l and 'google' not in l][:limit]
    except:
        return []

def search_surface_google(keyword, limit=5):
    try:
        url = f"https://www.google.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        return [l for l in links if l.startswith('http') and 'google.com' not in l][:limit]
    except:
        return []

def search_surface_bing(keyword, limit=5):
    try:
        url = f"https://www.bing.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        import re
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        return [l for l in links if 'bing.com' not in l and l.startswith('http')][:limit]
    except:
        return []

# ------------------------------------------------------------
# Dark Web Engines (10)
# ------------------------------------------------------------

def search_dark_ahmia(keyword, limit=10):
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

def search_dark_darksearchio(keyword, limit=10):
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

def search_dark_pyahmia(keyword, limit=10):
    try:
        from pyahmia import search
        onions = []
        for result in search(keyword, limit=limit):
            if result.get('link'):
                onions.append(result['link'])
        return onions[:limit]
    except:
        return []

def search_dark_onionsearch(keyword, limit=10):
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
            return [item['link'] for item in data if '.onion' in item.get('link', '')][:limit]
    except:
        pass
    return []

def search_dark_excavator(keyword, limit=10):
    try:
        url = f"https://excavator.app/api/search?q={quote_plus(keyword)}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return [item['url'] for item in data.get('results', []) if '.onion' in item.get('url', '')][:limit]
    except:
        pass
    return []

def search_dark_theseonion(keyword, limit=10):
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

# Placeholder for engines that require Tor or rarely work – they will return empty and be skipped
def search_dark_torch(keyword, limit=10):
    return []

def search_dark_phobos(keyword, limit=10):
    return []

def search_dark_deepwebsearch(keyword, limit=10):
    return []  # duplicate of ahmia, skip

def search_dark_fallback(keyword, limit=10):
    return []

# ------------------------------------------------------------
# Master search functions
# ------------------------------------------------------------

def search_web(keyword, limit=5):
    all_engines = [
        search_surface_duckduckgo, search_surface_qwant, search_surface_brave,
        search_surface_searxng, search_surface_mojeek, search_surface_yandex,
        search_surface_startpage, search_surface_ecosia, search_surface_google, search_surface_bing
    ]
    for eng in all_engines:
        try:
            res = eng(keyword, limit)
            if res:
                return res
        except:
            continue
    return []

def dark_web_search(keyword, limit=10):
    all_engines = [
        search_dark_ahmia, search_dark_darksearchio, search_dark_pyahmia,
        search_dark_onionsearch, search_dark_excavator, search_dark_theseonion,
        search_dark_torch, search_dark_phobos, search_dark_deepwebsearch, search_dark_fallback
    ]
    for eng in all_engines:
        try:
            res = eng(keyword, limit)
            if res:
                return res
        except:
            continue
    return []

def search_all(keyword):
    surface = search_web(keyword, limit=3)
    dark = dark_web_search(keyword, limit=5)
    return surface + dark

# ------------------------------------------------------------
if __name__ == "__main__":
    kw = "darknet market"
    print("Surface:", search_web(kw))
    print("Dark:", dark_web_search(kw))
    print("All:", search_all(kw))

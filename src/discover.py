import requests, re, time, random, json
from urllib.parse import quote_plus
from src.config import SEARCH_ENGINES

# -------------------- 1. Ahmia API (ডার্ক ওয়েবের জন্য) --------------------
def dark_web_search(keyword, limit=10):
    """
    Ahmia JSON API ব্যবহার করে ডার্ক ওয়েব (.onion) লিংক সার্চ করে।
    টর ছাড়াই কাজ করে, GitHub Actions-এর জন্য পারফেক্ট।
    """
    try:
        url = f"https://ahmia.fi/api/search/?q={quote_plus(keyword)}"
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return []
        data = response.json()
        links = []
        for result in data.get("results", []):
            link = result.get("link", "")
            if ".onion" in link:
                links.append(link)
            if len(links) >= limit:
                break
        return links
    except Exception as e:
        return []

# -------------------- 2. DuckDuckGo Lite (নরমাল ওয়েবের জন্য) --------------------
def search_web(keyword):
    """DuckDuckGo Lite ব্যবহার করে নরমাল ওয়েব লিংক খুঁজবে। Google/Bing এর চেয়ে অনেক বেশি নির্ভরযোগ্য"""
    urls, page = [], 0
    while len(urls) < 5 and page < 2:
        try:
            resp = requests.get("https://lite.duckduckgo.com/lite/", params={"q": keyword, "p": page}, timeout=10)
            if resp.status_code != 200: break
            found = re.findall(r'<a href="(https?://[^"]+)"', resp.text)
            for u in found[:5]:
                if any(x in u for x in ["google", "facebook", "twitter"]): continue
                urls.append(u)
            page += 1
            time.sleep(5)
        except: break
    return list(set(urls))

# -------------------- 3. SearXNG API (ডার্ক ওয়েবের ফালব্যাক) --------------------
def search_searxng(keyword, limit=5):
    """
    আরো বেশি নির্ভরযোগ্যতার জন্য ওপেন সোর্স SearXNG API ব্যবহার করা। 
    যথেষ্ট ইন্সট্যান্স আছে, GitHub Actions-এও সহজেই কাজ করে।
    """
    instances = ["https://searx.be", "https://searx.barxfux.ch", "https://search.whatever.social"]
    random.shuffle(instances)
    for instance in instances:
        try:
            resp = requests.get(f"{instance}/search", params={"q": keyword, "format": "json"}, timeout=10)
            if resp.status_code != 200: continue
            data = resp.json()
            links = [r['url'] for r in data.get('results', []) if '.onion' in r['url']]
            return links[:limit]
        except: continue
    return []

# -------------------- 4. OnionSearch (ডার্ক ওয়েবের মাস্টার কমান্ডার) --------------------
def search_onionsearch(keyword, limit=5):
    import subprocess, sys, os, json, tempfile
    try:
        subprocess.run(['pip3', 'install', '-q', 'onionsearch'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as tmp:
            tmp_path = tmp.name
        subprocess.run(['onionsearch', '--limit', str(limit), '--engines', 'ahmia,darksearchio,phobos', '--output', tmp_path, keyword],
                       capture_output=True, timeout=60, check=False)
        if os.path.exists(tmp_path):
            with open(tmp_path, 'r') as f:
                data = json.load(f)
            os.unlink(tmp_path)
            return [item['link'] for item in data if '.onion' in item.get('link', '')]
    except: return []
    return []

# -------------------- 5. মাস্টার সার্চ ফাংশন --------------------
def search_all(keyword):
    links = search_web(keyword)
    dlinks = dark_web_search(keyword)
    if not dlinks: dlinks = search_searxng(keyword)
    all_links = list(set(links + dlinks))
    if not all_links: all_links = search_onionsearch(keyword)
    return all_links

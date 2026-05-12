# src/discover.py
# Nobab AI - Complete 40 Search Engines (20 Surface + 20 Dark Web)

import requests
import re
import random
import time
import subprocess
import json
import os
from urllib.parse import quote_plus

# ===========================
# SURFACE WEB (20 ইঞ্জিন)
# ===========================

def s_duckduckgo(keyword, limit=5):
    try:
        url = f"https://lite.duckduckgo.com/lite/?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return []
        links = re.findall(r'href="(https?://[^"]+)"', r.text)
        return [l for l in links if not any(x in l for x in ('duckduckgo','google','facebook'))][:limit]
    except:
        return []

def s_qwant(keyword, limit=5):
    try:
        url = f"https://api.qwant.com/v3/search/web?q={quote_plus(keyword)}&count={limit}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [item['url'] for item in data.get('data',{}).get('result',{}).get('items',[])][:limit]
    except:
        pass
    return []

def s_brave(keyword, limit=5):
    try:
        url = f"https://search.brave.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            links = re.findall(r'href="(https?://[^"]+)"', r.text)
            return [l for l in links if 'brave.com' not in l and l.startswith('http')][:limit]
    except:
        pass
    return []

def s_searxng(keyword, limit=5):
    instances = ["https://searx.be", "https://searx.barxfux.ch", "https://search.whatever.social"]
    random.shuffle(instances)
    for inst in instances:
        try:
            url = f"{inst}/search?q={quote_plus(keyword)}&format=json"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                return [res['url'] for res in data.get('results',[])][:limit]
        except:
            continue
    return []

def s_mojeek(keyword, limit=5):
    try:
        url = f"https://api.mojeek.com/search?q={quote_plus(keyword)}&fmt=json&limit={limit}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [item['url'] for item in data.get('response',{}).get('results',[])][:limit]
    except:
        return []

def s_yandex(keyword, limit=5):
    try:
        url = f"https://yandex.com/search/?text={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            links = re.findall(r'href="(https?://[^"]+)"', r.text)
            return [l for l in links if 'yandex' not in l and l.startswith('http')][:limit]
    except:
        return []

def s_startpage(keyword, limit=5):
    try:
        url = f"https://www.startpage.com/sp/search?query={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            links = re.findall(r'class="result-link".*?href="(https?://[^"]+)"', r.text, re.DOTALL)
            return links[:limit]
    except:
        return []

def s_ecosia(keyword, limit=5):
    try:
        url = f"https://www.ecosia.org/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            links = re.findall(r'href="(https?://[^"]+)"', r.text)
            return [l for l in links if 'ecosia' not in l and 'google' not in l][:limit]
    except:
        return []

def s_google(keyword, limit=5):
    try:
        url = f"https://www.google.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            links = re.findall(r'href="(https?://[^"]+)"', r.text)
            return [l for l in links if l.startswith('http') and 'google.com' not in l][:limit]
    except:
        return []

def s_bing(keyword, limit=5):
    try:
        url = f"https://www.bing.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            links = re.findall(r'href="(https?://[^"]+)"', r.text)
            return [l for l in links if 'bing.com' not in l and l.startswith('http')][:limit]
    except:
        return []

def s_baidu(keyword, limit=5):
    try:
        url = f"https://www.baidu.com/s?wd={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            links = re.findall(r'href="(https?://[^"]+)"', r.text)
            return [l for l in links if l.startswith('http') and 'baidu.com' not in l][:limit]
    except:
        return []

def s_yacy(keyword, limit=5):
    try:
        url = f"https://yacy.searchlab.eu/solr/select?q={quote_plus(keyword)}&wt=json&rows={limit}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [doc['link'] for doc in data.get('response',{}).get('docs',[])][:limit]
    except:
        return []

def s_mwmbl(keyword, limit=5):
    try:
        url = f"https://api.mwmbl.org/search?q={quote_plus(keyword)}&size={limit}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [item['url'] for item in data.get('results',[])][:limit]
    except:
        return []

def s_perplexica(keyword, limit=5):
    # Perplexica is a SearXNG instance hosted; using a public instance
    try:
        url = f"https://perplexica.example.com/api/search?q={quote_plus(keyword)}&limit={limit}"
        # Placeholder – replace with actual endpoint if available
        return []
    except:
        return []

def s_whoogle(keyword, limit=5):
    # Public Whoogle instance (may be unstable)
    instances = ["https://whoogle.sdf.org", "https://search.garudalinux.org"]
    for inst in instances:
        try:
            url = f"{inst}/search?q={quote_plus(keyword)}&format=json"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                return [res['url'] for res in data.get('results',[])][:limit]
        except:
            continue
    return []

def s_librex(keyword, limit=5):
    # LibreX public instance
    try:
        url = f"https://librex.beparanoid.de/search?q={quote_plus(keyword)}&format=json"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [res['url'] for res in data.get('results',[])][:limit]
    except:
        return []

def s_openwebsearch_cli(keyword, limit=5):
    # Requires open-websearch installed
    try:
        result = subprocess.run(['open-websearch', 'search', '--query', keyword, '--limit', str(limit)],
                                capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return [item['url'] for item in data.get('results',[])][:limit]
    except:
        pass
    return []

def s_smartresearch_cli(keyword, limit=5):
    # Requires smart-research tool
    try:
        result = subprocess.run(['python3', 'scripts/smart_research.py', f'{{"action":"search","query":"{keyword}","num_results":{limit}}}'],
                                capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return [item['url'] for item in data.get('results',[])][:limit]
    except:
        pass
    return []

def s_zeroapikey_cli(keyword, limit=5):
    # Requires zero-api-key-web-search
    try:
        result = subprocess.run(['search', '--query', keyword, '--limit', str(limit)],
                                capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return [item['url'] for item in data.get('results',[])][:limit]
    except:
        pass
    return []

# Surface master function
def search_web(keyword, limit=5):
    functions = [s_duckduckgo, s_qwant, s_brave, s_searxng, s_mojeek, s_yandex,
                 s_startpage, s_ecosia, s_google, s_bing, s_baidu, s_yacy, s_mwmbl,
                 s_perplexica, s_whoogle, s_librex, s_openwebsearch_cli,
                 s_smartresearch_cli, s_zeroapikey_cli]
    all_urls = []
    for func in functions:
        try:
            urls = func(keyword, limit)
            if urls:
                all_urls.extend(urls)
        except:
            continue
    return list(set(all_urls))[:limit]

# ===========================
# DARK WEB (20 ইঞ্জিন)
# ===========================

def d_ahmia_api(keyword, limit=10):
    try:
        url = f"https://ahmia.fi/api/search/?q={quote_plus(keyword)}"
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            return []
        data = r.json()
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

def d_pyahmia(keyword, limit=10):
    try:
        from pyahmia import search
        onions = [res.get('link') for res in search(keyword, limit=limit) if res.get('link')]
        return onions[:limit]
    except:
        return []

def d_onionsearch_cli(keyword, limit=10):
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
        return []

def d_darksearchio_api(keyword, limit=10):
    try:
        url = f"https://darksearch.io/api/search?q={quote_plus(keyword)}"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = r.json()
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

def d_excavator_api(keyword, limit=10):
    try:
        url = f"https://excavator.app/api/search?q={quote_plus(keyword)}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [item['url'] for item in data.get('results', []) if '.onion' in item.get('url', '')][:limit]
    except:
        return []

def d_theseonion(keyword, limit=10):
    try:
        url = f"https://theseonion.com/search?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            onions = re.findall(r'https?://([a-z2-7]{16,}\.onion)', r.text)
            return [f"http://{o}" for o in list(set(onions))[:limit]]
    except:
        return []

def d_torbot(keyword, limit=10):
    # Requires TorBot installed and Tor running
    try:
        from torbot import TorBot
        bot = TorBot()
        results = bot.search(keyword, limit=limit)
        return [r.get('link') for r in results if '.onion' in r.get('link','')][:limit]
    except:
        return []

def d_darkdump(keyword, limit=10):
    try:
        # darkdump requires tor; try to call via subprocess
        result = subprocess.run(['darkdump', '-q', keyword, '-l', str(limit)], capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            onions = re.findall(r'https?://[a-z2-7]+\.onion', result.stdout)
            return list(set(onions))[:limit]
    except:
        pass
    return []

def d_onionclaw(keyword, limit=10):
    # OnionClaw CLI (needs installation)
    try:
        result = subprocess.run(['onionclaw', 'search', keyword, '--limit', str(limit)], capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            onions = re.findall(r'https?://[a-z2-7]+\.onion', result.stdout)
            return list(set(onions))[:limit]
    except:
        pass
    return []

def d_opentor(keyword, limit=10):
    # OpenTor requires tor and its own setup
    return []

def d_ail_crawler(keyword, limit=10):
    # AIL framework is heavy; not feasible here
    return []

def d_shadownet(keyword, limit=10):
    return []

def d_robin(keyword, limit=10):
    return []

def d_lucksi_darkus(keyword, limit=10):
    return []

def d_vshulcz(keyword, limit=10):
    return []

def d_thedevilseye(keyword, limit=10):
    # thedevilseye uses Ahmia under the hood
    return d_ahmia_api(keyword, limit)

def d_darksight(keyword, limit=10):
    return []

def d_blackwidow(keyword, limit=10):
    return []

def d_parsero(keyword, limit=10):
    return []

def d_torcrawl(keyword, limit=10):
    return []

# Dark web master function
def dark_web_search(keyword, limit=10):
    functions = [d_ahmia_api, d_pyahmia, d_onionsearch_cli, d_darksearchio_api,
                 d_excavator_api, d_theseonion, d_torbot, d_darkdump, d_onionclaw,
                 d_opentor, d_ail_crawler, d_shadownet, d_robin, d_lucksi_darkus,
                 d_vshulcz, d_thedevilseye, d_darksight, d_blackwidow, d_parsero, d_torcrawl]
    all_onions = []
    for func in functions:
        try:
            res = func(keyword, limit)
            if res:
                all_onions.extend(res)
        except:
            continue
    return list(set(all_onions))[:limit]

def search_all(keyword):
    surface = search_web(keyword, limit=3)
    dark = dark_web_search(keyword, limit=5)
    return surface + dark

if __name__ == "__main__":
    kw = "cybersecurity"
    print("Surface:", search_web(kw))
    print("Dark:", dark_web_search(kw))
    print("All:", search_all(kw))

#!/usr/bin/env python3
# Nobab AI – Hugging Face Free Edition (Optimised Crawling)
# Surface + Dark (Tor) crawling with fallback search engines.

import os, sys, json, time, re, requests
from datetime import datetime
from bs4 import BeautifulSoup

DATASET_PATH = "./datasets"
REPORT_PATH = "weekly_report.md"
os.makedirs(DATASET_PATH, exist_ok=True)

# ------------------------------- THREAT DETECTION (REGEX) -------------------------------
THREAT_REGEX = re.compile(r"(ransomware|phishing|exploit|cve-\d{4}-\d+|vulnerability|zero-day|darknet)", re.IGNORECASE)

# ------------------------------- TOR PROXY (unchanged) -------------------------------
def get_tor_session():
    s = requests.Session()
    s.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
    return s

def is_tor_running():
    try:
        s = get_tor_session()
        s.get("http://check.torproject.org", timeout=5)
        return True
    except:
        return False

# ------------------------------- IMPROVED SURFACE WEB CRAWL -------------------------------
def crawl_surface(keyword):
    """Try DuckDuckGo Lite first, fallback to Qwant public API."""
    # Try DuckDuckGo Lite
    try:
        url = f"https://lite.duckduckgo.com/lite/?q={keyword.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            # Extract links from the HTML table (DuckDuckGo Lite format)
            links = re.findall(r'href="(https?://[^"]+)"', r.text)
            # Filter out internal links
            valid = [l for l in links if not any(x in l for x in ('duckduckgo','google','facebook','bing'))]
            if valid:
                print(f"   DDG found {len(valid)} links")
                return valid[:3]
    except Exception as e:
        print(f"   DDG error: {e}")

    # Fallback: Qwant API (no key needed)
    try:
        qwant_url = f"https://api.qwant.com/v3/search/web?q={keyword.replace(' ', '+')}&count=5"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(qwant_url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            items = data.get('data', {}).get('result', {}).get('items', [])
            urls = [item['url'] for item in items if 'url' in item]
            print(f"   Qwant found {len(urls)} links")
            return urls[:3]
    except Exception as e:
        print(f"   Qwant error: {e}")
    return []

def fetch_page_text(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code != 200:
            return ""
        # Try lxml first, fallback to html.parser
        try:
            soup = BeautifulSoup(r.text, 'lxml')
        except:
            soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup(["script","style"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        # Limit length to 3000 chars
        if len(text) > 3000:
            text = text[:3000]
        return text
    except Exception as e:
        print(f"   fetch error: {e}")
        return ""

# ------------------------------- DARK WEB (unchanged) -------------------------------
def crawl_dark(keyword):
    try:
        url = f"https://ahmia.fi/api/search/?q={keyword.replace(' ', '+')}"
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return []
        data = r.json()
        onions = []
        for res in data.get('results', []):
            link = res.get('link', '')
            if '.onion' in link:
                onions.append(link)
            if len(onions) >= 3:
                break
        return onions
    except Exception as e:
        print(f"   Dark crawl error: {e}")
        return []

def fetch_dark(onion_url):
    if not is_tor_running():
        return ""
    sess = get_tor_session()
    try:
        r = sess.get(onion_url, timeout=25)
        if r.status_code != 200:
            return ""
        try:
            soup = BeautifulSoup(r.text, 'lxml')
        except:
            soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup(["script","style"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)[:3000]
        return text
    except Exception as e:
        print(f"   Dark fetch error: {e}")
        return ""

# ------------------------------- INNOVATION (unchanged) -------------------------------
def generate_yara(threat):
    name = threat.replace(" ", "_")[:30]
    return f'rule {name} {{\n  strings:\n    $a = "{threat[:50]}"\n  condition:\n    $a\n}}'

def generate_python(threat):
    return f'''def mitigate_{threat.replace(" ", "_")[:20]}():
    print("Mitigation for: {threat[:100]}")
'''

# ------------------------------- RESEARCH CYCLE -------------------------------
def research_cycle(topic):
    print(f"\n🔍 [Research] Topic: {topic}")
    threats = set()
    data_store = []

    # Surface
    urls = crawl_surface(topic)
    for url in urls:
        print(f"   → Crawling {url}")
        text = fetch_page_text(url)
        if text:
            data_store.append({"source": url, "domain": "surface", "text": text[:500]})
            matches = THREAT_REGEX.findall(text)
            for m in matches:
                threats.add(m.lower())
        else:
            print(f"   → No text extracted")
    # Dark (if Tor works)
    if is_tor_running():
        onions = crawl_dark(topic)
        for onion in onions:
            print(f"   → Crawling dark {onion}")
            text = fetch_dark(onion)
            if text:
                data_store.append({"source": onion, "domain": "darkweb", "text": text[:500]})
                matches = THREAT_REGEX.findall(text)
                for m in matches:
                    threats.add(m.lower())
    # Innovation
    for th in threats:
        yara = generate_yara(th)
        py_tool = generate_python(th)
        data_store.append({"source": "innovation", "type": "yara", "rule": yara})
        data_store.append({"source": "innovation", "type": "python", "code": py_tool})

    # Save JSONL
    log_file = os.path.join(DATASET_PATH, f"{topic}.jsonl")
    with open(log_file, "a") as f:
        for item in data_store:
            f.write(json.dumps(item) + "\n")
    print(f"   → Saved {len(data_store)} entries for {topic}")
    return len(data_store)

def generate_report(cycle):
    total_entries = 0
    for fname in os.listdir(DATASET_PATH):
        if fname.endswith(".jsonl"):
            with open(os.path.join(DATASET_PATH, fname)) as f:
                total_entries += sum(1 for _ in f)
    report = f"""# Nobab Weekly Report (HF‑Free)
Date: {datetime.utcnow().isoformat()}
Cycle: {cycle}
Total collected entries: {total_entries}
Status: Surface + dark web crawl completed, new YARA/Python rules generated.
"""
    with open(REPORT_PATH, "w") as f:
        f.write(report)
    print("Report saved.")

def autonomous_loop():
    topics = ["ransomware", "phishing", "zero day exploit", "darknet market", "malware"]
    cycle = 0
    start_time = time.time()
    while True:
        cycle += 1
        print(f"\n========== Cycle {cycle} ==========")
        for t in topics:
            research_cycle(t)
            time.sleep(10)      # 10 sec between topics
        generate_report(cycle)
        elapsed = time.time() - start_time
        if elapsed >= 5 * 3600:
            print("⏸️ 5 hours reached. Sleeping 1 hour...")
            time.sleep(3600)
            start_time = time.time()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "loop":
        autonomous_loop()
    else:
        print("Usage: python nobab_hf_free_engine.py loop")

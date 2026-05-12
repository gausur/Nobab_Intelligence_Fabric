#!/usr/bin/env python3
# Nobab AI – Hugging Face Free Edition (Optimised)
# Surface + Dark (Tor) crawling, threat detection (regex), YARA/Python generation.
# Each cycle saves data immediately to avoid GitHub runner termination.

import os, sys, json, time, re, requests
from datetime import datetime
from bs4 import BeautifulSoup

DATASET_PATH = "./datasets"
REPORT_PATH = "weekly_report.md"
os.makedirs(DATASET_PATH, exist_ok=True)

# ------------------------------- THREAT DETECTION (REGEX) -------------------------------
THREAT_REGEX = re.compile(r"(ransomware|phishing|exploit|cve-\d{4}-\d+|vulnerability|zero-day|darknet)", re.IGNORECASE)

# ------------------------------- TOR PROXY -------------------------------
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

# ------------------------------- SURFACE WEB (with fallback parser) -------------------------------
def fetch_surface(url):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        if r.status_code != 200:
            return ""
        # Try lxml first, fallback to html.parser
        try:
            soup = BeautifulSoup(r.text, 'lxml')
        except:
            soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup(["script","style"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except:
        return ""

def crawl_surface(keyword):
    try:
        url = f"https://lite.duckduckgo.com/lite/?q={keyword.replace(' ', '+')}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if r.status_code != 200:
            return []
        links = re.findall(r'href="(https?://[^"]+)"', r.text)
        return [l for l in links if not any(x in l for x in ('duckduckgo','google','facebook'))][:3]
    except:
        return []

# ------------------------------- DARK WEB (Tor) -------------------------------
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
    except:
        return []

def fetch_dark(onion_url):
    if not is_tor_running():
        return ""
    sess = get_tor_session()
    try:
        r = sess.get(onion_url, timeout=20)
        if r.status_code != 200:
            return ""
        try:
            soup = BeautifulSoup(r.text, 'lxml')
        except:
            soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup(["script","style"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except:
        return ""

# ------------------------------- INNOVATION (No LLM) -------------------------------
def generate_yara(threat):
    name = threat.replace(" ", "_")[:30]
    return f'rule {name} {{\n  strings:\n    $a = "{threat[:50]}"\n  condition:\n    $a\n}}'

def generate_python(threat):
    return f'''def mitigate_{threat.replace(" ", "_")[:20]}():
    print("Mitigation for: {threat[:100]}")
'''

# ------------------------------- RESEARCH CYCLE (SAVE PER CYCLE) -------------------------------
def research_cycle(topic):
    print(f"\n🔍 [Research] Topic: {topic}")
    threats = set()
    data_store = []

    # Surface
    urls = crawl_surface(topic)
    for url in urls:
        text = fetch_surface(url)
        if text:
            data_store.append({"source": url, "domain": "surface", "text": text[:500]})
            matches = THREAT_REGEX.findall(text)
            for m in matches:
                threats.add(m.lower())

    # Dark (if Tor works)
    if is_tor_running():
        onions = crawl_dark(topic)
        for onion in onions:
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

    # Save immediately to JSONL (so data isn't lost if runner stops)
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

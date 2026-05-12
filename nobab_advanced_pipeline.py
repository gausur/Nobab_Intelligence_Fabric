#!/usr/bin/env python3
"""
Nobab Advanced Pipeline – Semantic Dedup, Context Enrichment, API, Telegram Alert
All-in-one script. Does not modify any old file.
Reads ./datasets/*.jsonl and master_intel.jsonl (if exists).
Outputs: master_intel_clean.jsonl, enriched_master.jsonl, threats_api.json, telegram alert (optional)
"""

import os, json, re, subprocess, requests, hashlib
from collections import defaultdict
from datasketch import MinHash, MinHashLSH
from datetime import datetime

# ---------- CONFIG ----------
DATASET_DIR = "./datasets"
MASTER_INPUT = "master_intel.jsonl"
CLEAN_OUTPUT = "master_intel_clean.jsonl"
ENRICHED_OUTPUT = "enriched_master.jsonl"
API_OUTPUT = "threats_api.json"
REPORT_FILE = "semantic_dedup_report.md"
NUM_PERM = 128
THRESHOLD = 0.8
IP_PATTERN = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# ---------- 1. LOAD ALL TEXTS ----------
def load_texts():
    texts = []
    # Scan datasets folder
    if os.path.exists(DATASET_DIR):
        for root, _, files in os.walk(DATASET_DIR):
            for f in files:
                if f.endswith(".jsonl"):
                    with open(os.path.join(root, f), 'r') as fp:
                        for line in fp:
                            try:
                                data = json.loads(line)
                                txt = data.get("text") or data.get("snippet") or data.get("full_text") or str(data)
                                if len(txt) > 50:
                                    texts.append(txt)
                            except: pass
    # Also read existing master index
    if os.path.exists(MASTER_INPUT):
        with open(MASTER_INPUT, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    txt = data.get("full_text") or data.get("text_preview") or str(data)
                    if len(txt) > 50:
                        texts.append(txt)
                except: pass
    return texts

# ---------- 2. SEMANTIC DEDUP (MinHash + LSH) ----------
def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]", " ", text)
    words = text.split()
    shingles = set()
    for i in range(len(words)-2):
        shingles.add(" ".join(words[i:i+3]))
    return shingles

def get_minhash(text):
    m = MinHash(num_perm=NUM_PERM)
    for sh in tokenize(text):
        m.update(sh.encode('utf8'))
    return m

def deduplicate(texts):
    lsh = MinHashLSH(threshold=THRESHOLD, num_perm=NUM_PERM)
    minhashes = {}
    unique = []
    for i, txt in enumerate(texts):
        m = get_minhash(txt)
        minhashes[i] = m
        if not lsh.query(m):
            lsh.insert(str(i), m)
            unique.append(txt)
    return unique

# ---------- 3. CONTEXT ENRICHMENT (WHOIS) ----------
def enrich_ip(ip):
    try:
        result = subprocess.run(["whois", ip], capture_output=True, text=True, timeout=5)
        for line in result.stdout.splitlines()[:10]:
            if "descr" in line.lower() or "country" in line.lower() or "org" in line.lower():
                return line.strip()
        return "No info"
    except:
        return "Whois failed"

def enrich_text(text):
    ips = IP_PATTERN.findall(text)
    enriched = []
    for ip in set(ips[:3]):
        enriched.append({"ip": ip, "whois": enrich_ip(ip)})
    return enriched

# ---------- 4. GENERATE API FILE (threats_api.json) ----------
def generate_api(unique_texts):
    threats = []
    for txt in unique_texts[:100]:
        threats.append({
            "timestamp": datetime.utcnow().isoformat(),
            "snippet": txt[:200],
            "enrichment": enrich_text(txt)   # lightweight, can be skipped
        })
    with open(API_OUTPUT, "w") as f:
        json.dump({"last_updated": datetime.utcnow().isoformat(), "threats": threats}, f, indent=2)
    print(f"✅ API saved: {API_OUTPUT}")

# ---------- 5. TELEGRAM ALERT (OPTIONAL) ----------
def send_telegram(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials missing. Skipping alert.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message}, timeout=5)
        print("Telegram alert sent.")
    except Exception as e:
        print(f"Telegram error: {e}")

# ---------- 6. MAIN PIPELINE ----------
def main():
    print("🔍 Loading all texts from datasets and master index...")
    all_texts = load_texts()
    print(f"   Total raw entries: {len(all_texts)}")
    if not all_texts:
        print("No data found.")
        return

    print("🧠 Performing semantic deduplication...")
    unique_texts = deduplicate(all_texts)
    print(f"   Unique after dedup: {len(unique_texts)} (removed {len(all_texts)-len(unique_texts)})")

    # Save clean master
    with open(CLEAN_OUTPUT, "w") as f:
        for txt in unique_texts:
            f.write(json.dumps({"text_preview": txt[:300], "full_text": txt}) + "\n")
    print(f"✅ Clean master saved: {CLEAN_OUTPUT}")

    # Generate enriched master (with whois)
    print("🌐 Enriching IPs (this may take a while)...")
    with open(ENRICHED_OUTPUT, "w") as f:
        for txt in unique_texts:
            entry = {"text_preview": txt[:300], "full_text": txt, "enrichment": enrich_text(txt)}
            f.write(json.dumps(entry) + "\n")
    print(f"✅ Enriched master saved: {ENRICHED_OUTPUT}")

    # Generate API
    generate_api(unique_texts)

    # Report
    report = f"""# Nobab Semantic Dedup Report
Original: {len(all_texts)}
Unique: {len(unique_texts)}
Duplicates removed: {len(all_texts)-len(unique_texts)}
Threshold: {THRESHOLD*100}%
"""
    with open(REPORT_FILE, "w") as f:
        f.write(report)
    print(f"📄 Report saved: {REPORT_FILE}")

    # Telegram alert (only if new threats)
    if unique_texts:
        send_telegram(f"🚨 Nobab AI: {len(unique_texts)} unique threats processed. Latest: {unique_texts[0][:100]}")

if __name__ == "__main__":
    main()

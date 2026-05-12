#!/usr/bin/env python3
# Nobab AI - Complete Query Engine (Standalone)
# No external files needed. Just run with python src/query_engine.py <source_type> <question>

import sys
import re
import requests
import chromadb
import time
from urllib.parse import quote_plus
from sentence_transformers import SentenceTransformer

# ---------------------------- CONFIGURATION ----------------------------
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "autonomous_intel"

# ---------------------------- SURFACE WEB SEARCH (DuckDuckGo Lite) ----------------------------
def search_surface(keyword, limit=3):
    """Search using DuckDuckGo Lite HTML (no API key)"""
    try:
        url = f"https://lite.duckduckgo.com/lite/?q={quote_plus(keyword)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return []
        # Extract URLs from HTML
        links = re.findall(r'href="(https?://[^"]+)"', resp.text)
        # Filter out internal links
        valid = [l for l in links if not any(x in l for x in ('duckduckgo', 'google', 'facebook', 'twitter'))]
        return valid[:limit]
    except Exception as e:
        print(f"Surface search error: {e}")
        return []

# ---------------------------- DARK WEB SEARCH (Ahmia API) ----------------------------
def search_dark(keyword, limit=3):
    """Search dark web using Ahmia JSON API (no Tor needed)"""
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
    except Exception as e:
        print(f"Dark search error: {e}")
        return []

# ---------------------------- CRAWL & EXTRACT TEXT ----------------------------
def crawl_and_extract(url):
    """Fetch URL, extract main text using trafilatura (fast)"""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            return ""
        # Use trafilatura for clean text extraction
        import trafilatura
        text = trafilatura.extract(resp.text, fast=True, include_comments=False, include_tables=False)
        if text:
            # Clean extra spaces
            text = re.sub(r'\s+', ' ', text).strip()
            return text[:2000]  # limit length
        return ""
    except Exception as e:
        print(f"Crawl error {url}: {e}")
        return ""

# ---------------------------- CHROMADB QUERY ----------------------------
def query_chromadb(query, top_k=3):
    """Search local ChromaDB and return results"""
    try:
        embedder = SentenceTransformer("all-MiniLM-L6-v2")
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        collection = client.get_collection(COLLECTION_NAME)
        q_emb = embedder.encode([query]).tolist()
        results = collection.query(query_embeddings=q_emb, n_results=top_k)
        if not results['documents'][0]:
            return []
        return list(zip(results['documents'][0], results['metadatas'][0]))
    except Exception as e:
        print(f"ChromaDB error: {e}")
        return []

# ---------------------------- MAIN ANSWER FUNCTION ----------------------------
def answer(query, source_type):
    print(f"\n🤔 প্রশ্ন: {query}")
    print(f"🎯 সোর্স: {source_type}\n")

    if source_type == "chromadb":
        results = query_chromadb(query)
        if results:
            print("✅ ChromaDB থেকে ফলাফল:")
            for i, (doc, meta) in enumerate(results):
                print(f"\n--- ফল {i+1} ---")
                print(f"URL: {meta.get('url', 'N/A')}")
                print(f"কীওয়ার্ড: {meta.get('keyword', 'N/A')}")
                print(doc[:500] + "..." if len(doc) > 500 else doc)
        else:
            print("❌ ChromaDB-তে কিছু পাওয়া যায়নি।")
        return

    # Live search (normal, darkweb, or both)
    urls = []
    if source_type in ["normal", "both"]:
        urls.extend(search_surface(query, limit=2))
    if source_type in ["darkweb", "both"]:
        urls.extend(search_dark(query, limit=2))
    
    if not urls:
        print("❌ কোনো সার্চ ফলাফল পাওয়া যায়নি।")
        return

    print(f"🔍 পেয়েছি {len(urls)} টি URL। ক্রল করছি...\n")
    all_texts = []
    for url in urls:
        print(f"   ক্রলিং: {url}")
        text = crawl_and_extract(url)
        if text:
            all_texts.append(text)
            print(f"      → {len(text)} অক্ষর ডেটা পাওয়া গেছে।")
        else:
            print(f"      → কোনো ডেটা পাওয়া যায়নি।")
        time.sleep(1)  # gentle delay

    if all_texts:
        print("\n🌍 লাইভ ওয়েব থেকে ফলাফল:")
        for i, text in enumerate(all_texts):
            print(f"\n--- ফল {i+1} ---")
            print(text[:600] + "..." if len(text) > 600 else text)
    else:
        print("❌ ক্রল করে কোনো টেক্সট বের করা যায়নি।")

# ---------------------------- COMMAND LINE HANDLER ----------------------------
def main():
    if len(sys.argv) < 3:
        print("ব্যবহার: python query_engine.py <source_type> <প্রশ্ন>")
        print("source_type: normal, darkweb, both, chromadb")
        print("উদাহরণ: python query_engine.py both \"What is ransomware?\"")
        return
    source_type = sys.argv[1].lower()
    query = ' '.join(sys.argv[2:])
    if source_type not in ["normal", "darkweb", "both", "chromadb"]:
        print("❌ ভুল source_type। normal, darkweb, both, chromadb দিন।")
        return
    answer(query, source_type)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# src/query_engine.py
# Nobab AI Query Engine: Search local ChromaDB + live dark/surface web

import sys
import requests
import chromadb
from urllib.parse import quote_plus
from sentence_transformers import SentenceTransformer
from src.config import CHROMA_DIR, COLLECTION_NAME
from src.discover import dark_web_search, search_web
from src.crawler import crawl_page
from src.processor import extract_clean_text, chunk_text

# Load embedding model and ChromaDB
embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(COLLECTION_NAME)

def query_chromadb(query, top_k=3):
    """Search local ChromaDB and return top result texts with metadata"""
    q_emb = embedder.encode([query]).tolist()
    results = collection.query(query_embeddings=q_emb, n_results=top_k)
    if not results['documents'][0]:
        return []
    return list(zip(results['documents'][0], results['metadatas'][0]))

def live_search_and_crawl(keyword, max_results=2):
    """Live search from surface + dark web, crawl and return cleaned text chunks"""
    print(f"🌐 Live searching for: {keyword}")
    urls = []
    # Surface web
    surface = search_web(keyword)
    urls.extend(surface[:max_results])
    # Dark web (Ahmia)
    dark = dark_web_search(keyword)
    urls.extend(dark[:max_results])
    
    all_texts = []
    for url in urls:
        print(f"   Crawling {url}")
        data = crawl_page(url, depth=1)
        if data:
            raw_text = data[0]["text"]
            clean = extract_clean_text(raw_text)
            if clean:
                all_texts.append(clean)
    return all_texts

def show_stored_info():
    """Display what data is currently stored in ChromaDB"""
    # Get collection count and sample metadata
    count = collection.count()
    if count == 0:
        print("📭 ChromaDB is empty. No data yet.")
        return
    print(f"📊 ChromaDB contains {count} chunks of text.")
    # Get all unique keywords from metadata
    all_meta = collection.get()['metadatas']
    keywords = set()
    urls = set()
    for m in all_meta:
        if m and 'keyword' in m:
            keywords.add(m['keyword'])
        if m and 'url' in m:
            urls.add(m['url'])
    print(f"🔑 Keywords stored: {', '.join(sorted(keywords))}")
    print(f"🌐 Source URLs: {', '.join(list(urls)[:5])} ... (first 5)")

def answer(query):
    print(f"\n🤔 Your question: {query}\n")
    # First try local ChromaDB
    local_results = query_chromadb(query)
    if local_results:
        print("✅ Found in local ChromaDB:")
        for i, (doc, meta) in enumerate(local_results):
            print(f"\n--- Result {i+1} ---")
            print(f"Source: {meta.get('url', 'unknown')}")
            print(f"Keyword: {meta.get('keyword', 'unknown')}")
            print(doc[:500] + "..." if len(doc) > 500 else doc)
        return
    else:
        print("⚠️ Not found in ChromaDB. Searching live...")
        live_texts = live_search_and_crawl(query)
        if live_texts:
            print("\n🌍 Live results:")
            for i, text in enumerate(live_texts[:2]):
                print(f"\n--- Result {i+1} ---")
                print(text[:500] + "..." if len(text) > 500 else text)
        else:
            print("❌ No results found from live search either.")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python src/query_engine.py 'your question'")
        print("  python src/query_engine.py --list")
        return
    arg = ' '.join(sys.argv[1:])
    if arg == '--list':
        show_stored_info()
    else:
        answer(arg)

if __name__ == "__main__":
    main()

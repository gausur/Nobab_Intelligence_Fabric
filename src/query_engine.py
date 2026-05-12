#!/usr/bin/env python3
import sys
import requests
import chromadb
from urllib.parse import quote_plus
from sentence_transformers import SentenceTransformer
from src.config import CHROMA_DIR, COLLECTION_NAME
from src.discover import dark_web_search, search_web
from src.crawler import crawl_page
from src.processor import extract_clean_text

embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(COLLECTION_NAME)

def query_chromadb(query, top_k=3):
    q_emb = embedder.encode([query]).tolist()
    results = collection.query(query_embeddings=q_emb, n_results=top_k)
    if not results['documents'][0]:
        return []
    return list(zip(results['documents'][0], results['metadatas'][0]))

def live_search(source_type, keyword, max_results=2):
    urls = []
    if source_type in ["normal", "both"]:
        urls.extend(search_web(keyword)[:max_results])
    if source_type in ["darkweb", "both"]:
        urls.extend(dark_web_search(keyword)[:max_results])
    if not urls:
        return []
    all_texts = []
    for url in urls:
        data = crawl_page(url, depth=1)
        if data:
            raw_text = data[0]["text"]
            clean = extract_clean_text(raw_text)
            if clean:
                all_texts.append(clean)
    return all_texts

def answer(query, source_type):
    print(f"\n🤔 প্রশ্ন: {query}")
    print(f"🎯 সোর্স: {source_type}\n")
    if source_type == "chromadb":
        local = query_chromadb(query)
        if local:
            print("✅ ChromaDB থেকে ফলাফল:")
            for i, (doc, meta) in enumerate(local):
                print(f"\n--- ফল {i+1} ---")
                print(f"URL: {meta.get('url', 'N/A')}")
                print(f"কীওয়ার্ড: {meta.get('keyword', 'N/A')}")
                print(doc[:500] + "..." if len(doc) > 500 else doc)
        else:
            print("❌ ChromaDB-তে কিছু পাওয়া যায়নি।")
    elif source_type in ["normal", "darkweb", "both"]:
        # ChromaDB search first if we want combined? Actually user may want only live.
        # For live only we skip ChromaDB. For both, we can first try ChromaDB then live.
        if source_type == "both":
            local = query_chromadb(query)
            if local:
                print("✅ ChromaDB থেকে ফলাফল (সর্বপ্রথম দেখানো হচ্ছে):")
                for i, (doc, meta) in enumerate(local):
                    print(f"\n--- ChromaDB ফল {i+1} ---")
                    print(doc[:300] + "..." if len(doc) > 300 else doc)
                print("\n🌐 এখন লাইভ ওয়েব থেকেও খুঁজছি...\n")
            else:
                print("⚠️ ChromaDB-তে কিছু নেই। লাইভ ওয়েব খুঁজছি...\n")
        live = live_search(source_type, query)
        if live:
            print("🌍 লাইভ ওয়েব থেকে ফলাফল:")
            for i, text in enumerate(live):
                print(f"\n--- লাইভ ফল {i+1} ---")
                print(text[:500] + "..." if len(text) > 500 else text)
        else:
            print("❌ লাইভ ওয়েবেও কিছু পাওয়া যায়নি।")
    else:
        print("❌ ভুল সোর্স টাইপ। `normal`, `darkweb`, `both`, অথবা `chromadb` ব্যবহার করুন।")

def main():
    if len(sys.argv) < 3:
        print("ব্যবহার: python query_engine.py <source_type> <প্রশ্ন>")
        print("source_type: normal, darkweb, both, chromadb")
        return
    source_type = sys.argv[1].lower()
    query = ' '.join(sys.argv[2:])
    answer(query, source_type)

if __name__ == "__main__":
    main()

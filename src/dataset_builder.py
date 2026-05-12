import os
import json
import time
from src.discover import search_web
from src.crawler import crawl_page
from src.processor import extract_clean_text, chunk_text
from src.embedder import add_to_vectorstore
from src.config import DATA_ROOT

def build_dataset(keywords=None):
    if keywords is None:
        keywords = ["ransomware", "phishing", "zero day exploit"]
    os.makedirs(DATA_ROOT, exist_ok=True)

    for kw in keywords:
        print(f"Searching for: {kw}")
        urls = search_web(kw)
        for url in urls[:3]:
            raw = crawl_page(url, depth=1)
            for item in raw:
                clean = extract_clean_text(item["text"])
                if not clean:
                    continue
                chunks = chunk_text(clean)
                for i, chunk in enumerate(chunks[:5]):
                    doc_id = f"{kw}_{hash(url)}_{i}"
                    meta = {"keyword": kw, "url": url, "timestamp": item["timestamp"]}
                    add_to_vectorstore(doc_id, chunk, meta)
        out_file = os.path.join(DATA_ROOT, f"{kw}.jsonl")
        with open(out_file, "w") as f:
            f.write(json.dumps({"keyword": kw, "time": time.time()}) + "\n")

if __name__ == "__main__":
    build_dataset()

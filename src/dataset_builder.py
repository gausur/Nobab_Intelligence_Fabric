import json
import os
import torch
import numpy as np
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from .crawler import crawl_page
from .discover import search_web
from .processor import extract_clean_text, chunk_text
from .embedder import add_to_vectorstore
from config import DATA_ROOT, CLASSIFIER_MODEL, CLASSIFIER_THRESHOLD, RELEVANCE_SCORE_THRESHOLD

# 🧠 MITRE ATT&CK ক্লাসিফায়ার লোড
tokenizer = AutoTokenizer.from_pretrained(CLASSIFIER_MODEL)
model = AutoModelForSequenceClassification.from_pretrained(
    CLASSIFIER_MODEL,
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32
)
model.eval()

def calculate_relevance_score(text, tactic_labels):
    """ML মডেল ব্যবহার করে রেলেভ্যান্স স্কোর বের করে (0-100)"""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(logits.squeeze().cpu())
    # সর্বোচ্চ প্রোবাবিলিটি ট্যাকটিকের স্কোর নেওয়া
    max_prob = torch.max(probs).item()
    score = int(max_prob * 100)        # 0-100 স্কেলে রূপান্তর
    return score

def build_datasets(domains=None):
    if domains is None:
        domains = ["ransomware", "apt attack", "zero day exploit", "phishing kit", "cyber threat intel"]

    for domain in domains:
        print(f"🔍 Discovering for {domain}")
        urls = search_web(domain)
        print(f"Found {len(urls)} candidate URLs")

        for url in urls[:20]:
            print(f"  Crawling {url}")
            raw_data = crawl_page(url, depth=1)
            for item in raw_data:
                clean_text = extract_clean_text(item["text"])
                if not clean_text:
                    continue

                # 🤖 ML মডেল দিয়ে স্কোর বের করা
                score = calculate_relevance_score(clean_text, [domain])
                if score < RELEVANCE_SCORE_THRESHOLD:
                    print(f"Skipping low-relevance content (score {score} < {RELEVANCE_SCORE_THRESHOLD})")
                    continue

                chunks = chunk_text(clean_text)
                for i, chunk in enumerate(chunks):
                    doc_id = f"{domain}_{hash(url)}_{i}"
                    meta = {"domain": domain, "url": url, "timestamp": item["timestamp"], "relevance_score": score}
                    add_to_vectorstore(doc_id, chunk, meta)

        # ডেটাসেট সেভ (JSONL ফরম্যাটে)
        save_dataset(domain)

def save_dataset(domain):
    """সংগৃহীত ডেটা JSONL ফাইল হিসেবে সেভ করা"""
    os.makedirs(f"{DATA_ROOT}/{domain}", exist_ok=True)
    # ChromaDB কালেকশন থেকে সব ডেটা নিয়ে JSONL তৈরি
    import chromadb
    from config import CHROMA_DIR, COLLECTION_NAME
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_collection(COLLECTION_NAME)
    data = collection.get(where={"domain": domain})
    path = f"{DATA_ROOT}/{domain}/dataset_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.jsonl"
    with open(path, "w", encoding="utf-8") as f:
        for i in range(len(data["ids"])):
            record = {
                "id": data["ids"][i],
                "document": data["documents"][i],
                "metadata": data["metadatas"][i],
                "embedding": data["embeddings"][i] if data["embeddings"] else None
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"Saved dataset: {path}")

if __name__ == "__main__":
    build_datasets()

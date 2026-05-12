import os
from dotenv import load_dotenv

load_dotenv()

DATA_ROOT = "./datasets"
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "autonomous_intel"
TOR_PROXY = os.getenv("TOR_PROXY", None)
AHMIA_ENABLED = os.getenv("AHMIA_ENABLED", "true").lower() == "true"
SEARCH_ENGINES = {
    "google": "https://www.google.com/search?q=",
    "bing": "https://www.bing.com/search?q=",
    "ahmia": "https://ahmia.fi/search/?q="
}
CLASSIFIER_MODEL = "sarahwei/MITRE-v16-tactic-bert-case-based"  # MITRE ATT&CK ভিত্তিক স্কোরিং মডেল
CLASSIFIER_THRESHOLD = 0.5     # সিগময়েড প্রোবাবিলিটি থ্রেশহোল্ড
RELEVANCE_SCORE_THRESHOLD = 70  # ১-১০০ স্কেলে, MITRE স্কোর ভিত্তিতে তৈরি

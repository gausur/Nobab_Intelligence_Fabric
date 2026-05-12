import requests
from urllib.parse import quote_plus
from src.config import SEARCH_ENGINES

def search_web(keyword):
    """
    এই ফাংশনটি সারফেস ওয়েবের জন্য Google/Bing ব্যবহার করে।
    ডার্ক ওয়েবের জন্য আলাদা ফাংশন তৈরি করতে হবে (নিচে দেখুন)।
    """
    urls = []
    for engine, base in SEARCH_ENGINES.items():
        try:
            resp = requests.get(base + quote_plus(keyword), timeout=10)
            if resp.status_code == 200:
                import re
                links = re.findall(r'href=[\'"]?(https?://[^\'" >]+)', resp.text)
                urls.extend(links[:5])
        except:
            pass
    return list(set(urls))

if __name__ == "__main__":
    print(search_web("cybersecurity"))

import trafilatura
import re
import html
from tqdm import tqdm

def extract_clean_text(html_content):
    """trafilatura দিয়ে মূল টেক্সট বের করে"""
    if not html_content:
        return ""
    text = trafilatura.extract(html_content, include_comments=False, include_tables=False)
    if text:
        # এইচটিএমএল আনএস্কেপ এবং অতিরিক্ত হোয়াইটস্পেস পরিষ্কার
        text = html.unescape(text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return ""

def chunk_text(text, max_len=1000):
    """বাক্য অনুযায়ী টেক্সট ছোট ছোট ভাগে ভাগ করা"""
    if not text:
        return []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current = ""
    for sent in sentences:
        if len(current) + len(sent) < max_len:
            current += sent + " "
        else:
            if current:
                chunks.append(current.strip())
            current = sent + " "
    if current:
        chunks.append(current.strip())
    return chunks

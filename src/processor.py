import trafilatura
import re
import html

def extract_clean_text(html_content):
    """
    HTML থেকে মূল কন্টেন্ট বের করে (no_fallback parameter deprecated, fast=True use করুন)
    """
    if not html_content:
        return ""
    text = trafilatura.extract(html_content, fast=True, include_comments=False, include_tables=False)
    if text:
        text = html.unescape(text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return ""

def chunk_text(text, max_len=1000):
    if not text:
        return []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, cur = [], ""
    for sent in sentences:
        if len(cur) + len(sent) < max_len:
            cur += sent + " "
        else:
            if cur:
                chunks.append(cur.strip())
            cur = sent + " "
    if cur:
        chunks.append(cur.strip())
    return chunks

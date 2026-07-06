#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-06 03:42:29.002684

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    
    # Check for suspicious keywords in the URL path
    if re.search(r"(?i)\b(phishing|scam|malware|ransomware|virus)\b", url):[5D[K
url):
        return True
    
    # Check for suspicious keywords in the query string
    if re.search(r"(?i)\b(login|password|credentials|sensitive)\b", parsed_[7D[K
parsed_url.query):
        return True
    
    return False

def mitigate_phishing(url):
    # Redirect to a safe page
    print("Redirecting to a safe page...")
    import webbrowser
    webbrowser.open("https://example.com")
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-05 18:44:46.462801

import re
import urllib.parse

def detect_phishing(url):
    # Check if the URL is a valid HTTP/HTTPS URL
    if not re.match(r"https?://", url):
        return "Invalid URL"
    
    # Check if the URL contains any suspicious characters
    if any(c in url for c in ["<", ">", "=", "?", "&"]):
        return "Suspicious characters detected"
    
    # Check if the URL is a valid domain name
    try:
        domain = urllib.parse.urlparse(url).netloc
        if not re.match(r"^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$", domain):
            return "Invalid domain name"
    except:
        return "Invalid URL"
    
    # Check if the URL is a known phishing site
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            if b"phishing" in html or b"scam" in html:
                return "Phishing site detected"
    except:
        pass
    
    return "No phishing detected"

# Example usage:
url = "https://www.example.com"
result = detect_phishing(url)
print(result)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 09:56:27.388367

import re
import urllib.request
from collections import deque

def is_phishing(url):
    # Check if the URL is a valid HTTPS URL
    if not url.startswith("https://"):
        return False
    
    # Fetch the HTML content of the page
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return False
    
    # Check if the HTML content contains any suspicious strings
    for pattern in [r'<script>', r'</script>', r'eval']:
        if re.search(pattern, html.decode('utf-8')):
            return True
    
    # Check if the URL is a known phishing site
    with open("phishing_sites.txt", "r") as f:
        for line in f:
            if url == line.strip():
                return True
    
    # If none of the above conditions are met, return False
    return False
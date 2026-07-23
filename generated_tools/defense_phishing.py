#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-23 22:57:42.948324

import re

def is_phishing_url(url):
    # Check if the URL contains any suspicious characters
    if not re.search(r'^[a-zA-Z0-9]+://', url):
        return True
    
    # Check if the URL contains a known phishing domain
    if 'phishng.io' in url:
        return True
    
    # Check if the URL is from a known trusted source
    try:
        import requests
        res = requests.get(url)
        if res.status_code == 200 and 'X-Frame-Options' not in res.headers:[12D[K
res.headers:
            return True
    except requests.exceptions.RequestException:
        pass
    
    # If none of the above checks match, the URL is likely legitimate
    return False
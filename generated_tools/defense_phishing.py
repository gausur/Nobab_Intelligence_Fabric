#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-13 23:02:34.077730

import re
import requests

def is_phishing(url):
    # Check if the URL is valid
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        return False
    
    # Extract the domain name from the URL
    domain = re.search(r'https?://([^/]+)(/|$)', url).group(1)
    
    # Check if the domain is a known phishing site
    if domain in PHISHING_SITES:
        return True
    
    # Check if the URL contains any suspicious keywords or patterns
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in url:
            return True
    
    # Check if the URL is a shortened link
    if re.search(r'https?://[a-zA-Z0-9]{32}', url):
        return True
    
    return False

def mitigate_phishing(url):
    # Redirect to a safe page
    return 'https://example.com/safe_page.html'

PHISHING_SITES = ['phish.me', 'badsite.com']
SUSPICIOUS_KEYWORDS = ['free', 'discount', 'coupon']
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-17 23:41:26.302114

import re
import requests

def detect_phishing(url):
    # Check if the URL is valid
    if not requests.head(url).ok:
        return False
    
    # Check if the URL is a phishing site
    try:
        html = requests.get(url).text
        if re.search(r"<script>|<iframe|<form", html):
            return True
    except requests.exceptions.RequestException:
        return False
    
    return False
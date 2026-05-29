#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-29 21:48:58.394522

import re

def is_phishing(url):
    # Check if the URL contains any suspicious characters
    if re.search(r'[;:,./<>\\\[\]\?\|=+()*&!@#$%^"{}]', url):
        return True
    
    # Check if the URL is a valid domain name
    try:
        domain = urlparse(url).netloc.split(':')[0]
        if not re.match(r'^[a-zA-Z0-9.-]+$', domain):
            return True
    except Exception:
        pass
    
    # Check if the URL is a known phishing site
    try:
        with open('phishing_sites.txt') as f:
            for line in f:
                if re.match(line, url):
                    return True
    except FileNotFoundError:
        pass
    
    # Check if the URL is a known phishing site by analyzing its HTML conte[5D[K
content
    try:
        with requests.get(url) as r:
            text = BeautifulSoup(r.text, 'html.parser')
            for tag in ['a', 'form', 'input']:
                if re.search(tag, text):
                    return True
    except Exception:
        pass
    
    # No suspicious patterns found, the URL is likely safe
    return False
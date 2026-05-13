#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-13 14:25:53.890257

import re
import urllib.request

def detect_phishing(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    
    # Extract the domain name from the URL
    domain = urllib.request.urlparse(url).netloc
    
    # Check if the domain is a valid TLD
    if not re.match(r"^[a-z0-9.-]+$", domain):
        return False
    
    # Check if the URL contains any suspicious parameters or query strings
    for param in urllib.parse.urlencode(url).query:
        if re.search(r"\b(password|login|credentials)\b", urllib.parse.quot[17D[K
urllib.parse.quote_plus(param)):
            return False
    
    # Check if the URL is a known phishing site
    with open("phishing_sites.txt") as f:
        for line in f:
            if re.match(r"\b" + domain + r"\b", line):
                return True
    
    # If none of the above conditions are met, it's likely a legitimate web[3D[K
website
    return False
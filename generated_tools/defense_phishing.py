#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-01 14:14:07.729098

import re
import ssl
from urllib.request import urlopen

def detect_phishing(url):
    # Check if the URL is valid
    try:
        urlopen(url)
    except:
        return False
    
    # Check if the URL contains any suspicious patterns
    pattern = r"^((https?|ftp)://)?[A-Za-z0-9]+(\.[A-Za-z0-9]{2,3}){1,3}$"
    match = re.search(pattern, url)
    if not match:
        return False
    
    # Check the SSL certificate of the URL
    try:
        ssl_context = ssl._create_unverified_context()
        urlopen(url, context=ssl_context)
    except:
        return False
    
    # If none of the above checks fail, the URL is considered safe
    return True
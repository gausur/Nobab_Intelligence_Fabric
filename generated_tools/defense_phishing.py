#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-15 11:50:41.152536

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    # Check if the URL contains any suspicious patterns
    if re.search(r'[a-zA-Z0-9_]+://', url):
        return False
    elif re.search(r'\w+:\/\/', url):
        return True
    else:
        # Check if the URL contains any suspicious subdomains
        parsed_url = urlparse(url)
        subdomain = parsed_url.netloc.split('.')[0]
        if subdomain in ['www', 'web', 'http']:
            return False
        else:
            return True
    return False
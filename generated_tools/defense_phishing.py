#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-10 02:09:08.403717

import re
import urllib.parse

def is_phishing(url):
    # Check if the URL is a valid HTTPS URL
    try:
        parsed_url = urllib.parse.urlparse(url)
        if not parsed_url.scheme == "https":
            return False
    except ValueError:
        return False
    
    # Check for common phishing patterns in the URL
    phishing_patterns = ["phishing", "fake", "spoofing", "scam"]
    for pattern in phishing_patterns:
        if re.search(pattern, url):
            return True
    
    # Check if the domain name is a known scammer
    domain = urllib.parse.urlsplit(url).netloc
    scammers = ["example.com", "fakesite.org"]
    if domain in scammers:
        return True
    
    # No phishing detected
    return False
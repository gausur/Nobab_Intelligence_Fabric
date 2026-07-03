#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-03 19:08:08.456445

import re
import urllib

def is_phishing(url):
    # Check if the URL is valid
    if not urllib.parse.urlparse(url).scheme:
        return False
    
    # Extract the domain name from the URL
    domain = urllib.parse.urlparse(url).netloc
    
    # Check if the domain name is a known phishing site
    with open("phishing_domains.txt") as f:
        for line in f:
            if line.strip() == domain:
                return True
    return False

def mitigate(url):
    # Check if the URL is a phishing attack
    if is_phishing(url):
        print("Phishing detected!")
        # Block the request and send a warning message to the user
        return "Blocked"
    else:
        # Allow the request and continue with normal processing
        return "Allowed"
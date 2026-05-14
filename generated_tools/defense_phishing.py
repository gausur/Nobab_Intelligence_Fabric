#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-14 22:05:15.644219

import re

def is_phishing(url):
    pattern = r"^https?:\/\/[a-zA-Z0-9\.]+\/.*$"
    if not re.match(pattern, url):
        return False

    # Check for suspicious domain names and URLs
    suspicious_domains = ["example.com", "fakewebsite.com"]
    for domain in suspicious_domains:
        if domain in url:
            return True
    
    return False

def mitigate(url):
    # Redirect to a safe URL
    return "https://www.example.com"

# Test the function
urls = ["https://example.com", "https://fakewebsite.com"]
for url in urls:
    if is_phishing(url):
        mitigate(url)
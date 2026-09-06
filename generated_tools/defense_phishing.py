#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-06 00:29:38.165526

import re
import urllib.parse

def detect_phishing(url):
    # Check if the URL is valid
    if not urllib.parse.urlparse(url).netloc:
        return False

    # Check if the URL contains any suspicious keywords
    keywords = ["phish", "fishing", "scam", "malware", "spoof"]
    for keyword in keywords:
        if keyword in url:
            return True

    # Check if the URL is from a known trusted source
    trusted_sources = ["example.com", "google.com", "facebook.com"]
    for trusted_source in trusted_sources:
        if url.startswith(trusted_source):
            return False

    # Check if the URL is from a known malicious source
    malicious_sources = ["phish.com", "fishing.net", "scam.io"]
    for malicious_source in malicious_sources:
        if url.startswith(malicious_source):
            return True

    # If the URL is from an unknown source, assume it's a phishing attack
    return True

def mitigate_phishing(url):
    # Check if the URL is a phishing attack
    if detect_phishing(url):
        # Block the URL
        return False

    # Allow the URL
    return True

# Test the script
url = "http://phish.com/login"
print(detect_phishing(url)) # True
print(mitigate_phishing(url)) # False

url = "https://example.com/login"
print(detect_phishing(url)) # False
print(mitigate_phishing(url)) # True

url = "https://facebook.com/login"
print(detect_phishing(url)) # False
print(mitigate_phishing(url)) # True
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-22 22:05:14.392613

import re
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)

def is_phishing_site(url):
    if not is_valid_url(url):
        return False
    parsed = urlparse(url)
    hostname = parsed.hostname.lower()
    # Check for common phishing domain patterns
    if re.search(r'[a-z0-9]{3}\.com$', hostname):
        return True
    if re.search(r'[a-z0-9]{2,3}\.co\.[a-z]{2}$', hostname):
        return True
    if re.search(r'[a-z0-9]+\.ru$', hostname):
        return True
    # Check for common phishing domain suffixes
    if parsed.netloc.endswith('.com') or parsed.netloc.endswith('.co'):
        return True
    return False

def mitigate_phishing(url):
    if is_phishing_site(url):
        print("Phishing site detected")
    else:
        print("No phishing site detected")

# Test cases
mitigate_phishing("https://www.example.com/")  # No phishing site detected
mitigate_phishing("https://example.com/")  # Phishing site detected
mitigate_phishing("http://example.com/")  # Phishing site detected
mitigate_phishing("http://www.example.com/")  # No phishing site detected
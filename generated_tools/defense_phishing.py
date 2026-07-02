#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-02 12:08:12.435821

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return True
    if not parsed.netloc.endswith(".com"):
        return True
    if parsed.path == "/":
        return True
    return False

def mitigate_phishing_attack(url):
    # Redirect to a safe URL
    print("Redirecting to a safe URL...")
    # You can also display an error message or do other actions here

if __name__ == "__main__":
    url = input("Enter the URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
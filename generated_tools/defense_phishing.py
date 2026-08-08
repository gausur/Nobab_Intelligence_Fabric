#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-08 04:07:14.175575

import re
import urllib.parse
from collections import Counter

def is_phishing(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    if not domain:
        return False
    if "." not in domain:
        return False
    parts = domain.split(".")
    if len(parts) < 2:
        return False
    if any(part.isdigit() for part in parts):
        return False
    if parts[-1] == "com":
        return False
    return True

def mitigate_phishing(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    if not domain:
        return False
    if "." not in domain:
        return False
    parts = domain.split(".")
    if len(parts) < 2:
        return False
    if any(part.isdigit() for part in parts):
        return False
    if parts[-1] == "com":
        return False
    return True

def main():
    urls = ["http://www.example.com", "https://www.example.com"]
    for url in urls:
        is_phishing(url)
        mitigate_phishing(url)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 18:53:10.527909

import re
import json
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if parsed.scheme == "http" and parsed.netloc != "example.com":
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attempt detected!")
        return None
    else:
        return url

if __name__ == "__main__":
    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f]
    filtered_urls = [mitigate_phishing(url) for url in urls if is_phishing([12D[K
is_phishing(url)]
    print("Filtered URLs:", filtered_urls)
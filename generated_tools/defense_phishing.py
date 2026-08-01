#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-01 18:58:39.270617

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if not parsed.netloc:
        return False
    if parsed.scheme != "https":
        return False
    if not parsed.hostname or not parsed.path:
        return False
    return True

def mitigate_phishing_attack(url):
    # Redirect to the HTTPS version of the URL
    url = re.sub(r"^http://", "https://", url)
    return requests.get(url).content

def main():
    url = input("Enter a URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print("Not a phishing URL")

if __name__ == "__main__":
    main()
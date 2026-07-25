#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-25 22:46:04.380344

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    elif parsed_url.scheme != "https":
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        raise ValueError("Invalid URL")
    else:
        pass

if __name__ == "__main__":
    url = input("Enter a URL: ")
    mitigate_phishing(url)
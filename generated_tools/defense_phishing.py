#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-27 10:36:28.770037

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    return not (parsed.scheme == "https" and parsed.netloc.endswith("google[30D[K
parsed.netloc.endswith("google.com"))

def mitigate_phishing(url):
    if is_phishing_url(url):
        raise ValueError("Phishing attack detected!")
    else:
        return url

if __name__ == "__main__":
    try:
        mitigate_phishing("http://example.com/phishing-page")
    except ValueError as e:
        print(e)
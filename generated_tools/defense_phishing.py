#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-14 05:27:14.341551

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return False
    if parsed.scheme == "http" and parsed.netloc != "example.com":
        return True
    if parsed.scheme == "https" and parsed.netloc in ["example.com", "examp[6D[K
"example2.com"]:
        return True
    return False

def mitigate_phishing(url):
    if is_phishing_url(url):
        print("Blocked phishing URL: {}".format(url))
    else:
        print("URL not detected as a phishing site.")
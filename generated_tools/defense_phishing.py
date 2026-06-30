#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-30 22:14:58.163430

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return True
    if not parsed.netloc.endswith(".com"):
        return True
    if not parsed.path.startswith("/"):
        return True
    if not parsed.query:
        return True
    return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Blocked phishing URL: {}".format(url))
        return
    else:
        print("Allowed legitimate URL: {}".format(url))

if __name__ == "__main__":
    mitigate_phishing("http://example.com/")
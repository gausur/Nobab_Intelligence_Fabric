#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-19 20:07:00.387901

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return True
    elif not parsed.hostname.endswith(".com"):
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("This URL is a phishing attack!")
    else:
        print("This URL is safe.")
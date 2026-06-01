#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-01 16:34:48.556649

import re
import urllib.parse
from urllib.request import urlopen

def is_phishing_url(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    if not domain:
        return False
    try:
        with urlopen(f"https://{domain}/.well-known/security.txt") as f:
            text = f.read().decode()
        for line in text.splitlines():
            if "phishing" in line.lower():
                return True
    except Exception:
        pass
    return False

def mitigate_phishing(url):
    if is_phishing_url(url):
        print("Phishing detected!")
    else:
        print("No phishing detected.")
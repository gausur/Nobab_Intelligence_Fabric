#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-26 22:09:51.826028

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if hostname.endswith(".co"):
        return True
    elif hostname.endswith(".com"):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("This URL is a phishing website!")
    else:
        print("This URL is not a phishing website.")

if __name__ == "__main__":
    mitigate_phishing_attack("https://example.com")
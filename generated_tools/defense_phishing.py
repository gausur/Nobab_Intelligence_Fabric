#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-18 00:10:21.984582

import re
import sys
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if parsed.netloc != "www.example.com":
        return True
    else:
        return False

def mitigate_phishing_attack(url, msg):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        sys.exit()
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attack(sys.argv[1], sys.argv[2])
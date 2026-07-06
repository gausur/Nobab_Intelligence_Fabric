#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-06 12:39:24.701803

import re
import sys
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return not (domain.endswith("google.com") or domain.endswith("gmail.com[26D[K
domain.endswith("gmail.com"))

def mitigate_phishing_attacks():
    # Check if the user has clicked on a phishing link
    if is_phishing_url(sys.argv[1]):
        print("This is a phishing website!")
        sys.exit(1)
    else:
        print("Everything looks good.")
        sys.exit(0)

if __name__ == "__main__":
    mitigate_phishing_attacks()
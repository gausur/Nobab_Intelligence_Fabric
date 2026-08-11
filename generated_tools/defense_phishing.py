#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 17:53:05.421851

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if parsed.scheme != "http" and parsed.scheme != "https":
        return False
    if not parsed.netloc:
        return False
    if re.search(r"\.(com|org|gov|edu)$", parsed.netloc):
        return True
    else:
        return False

def mitigate_phishing_attack():
    print("Phishing attack detected!")
    # TODO: Add logic to block the user from accessing the phishing site
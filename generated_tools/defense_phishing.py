#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-24 09:19:00.373709

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if not parsed.netloc:
        return False
    tlds = ["com", "org", "edu"]
    for tld in tlds:
        if parsed.netloc.endswith("." + tld):
            return True
    return False

def mitigate_phishing(url):
    if is_phishing(url):
        raise ValueError("Phishing attack detected")

mitigate_phishing("https://www.example.com")  # Throws a ValueError
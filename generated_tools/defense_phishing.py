#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-23 09:21:29.810796

import re

def is_phishing_url(url):
    pattern = r"^https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attacks(url):
    if is_phishing_url(url):
        return "Invalid URL"
    else:
        return "Valid URL"

url = "https://www.example.com"
print(mitigate_phishing_attacks(url))
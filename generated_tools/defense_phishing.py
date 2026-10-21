#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-21 15:48:07.279854

import re

def is_phishing_url(url):
    # Check if the URL is a phishing URL
    if re.search(r"[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+.[a-zA-Z0-9-_]+", url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    # Redirect the user to a safe URL
    if is_phishing_url(url):
        return "https://www.example.com"
    else:
        return url

url = "http://example.com"

if is_phishing_url(url):
    mitigate_phishing_attack(url)
else:
    print("The URL is not a phishing URL.")
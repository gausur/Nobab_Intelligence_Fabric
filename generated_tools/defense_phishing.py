#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-17 21:03:08.277755

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return False
    for domain in ["example.com", "google.com"]:
        if parsed_url.netloc.endswith(domain):
            return True
    return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attack("https://www.example.com")
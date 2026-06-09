#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-09 10:56:24.694225

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        return False
    if hostname == "example.com":
        return True
    return False

def mitigate_phishing_attack(url):
    print("Phishing attack detected!")
    print("Please report this incident to the security team.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
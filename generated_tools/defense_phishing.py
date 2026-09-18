#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-18 07:48:34.374825

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith(".com"):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        return "Blocked"
    else:
        return "Allowed"

if __name__ == "__main__":
    url = input("Enter URL: ")
    result = mitigate_phishing_attack(url)
    print(result)
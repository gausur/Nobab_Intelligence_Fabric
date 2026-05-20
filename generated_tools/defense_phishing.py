#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-19 23:58:31.354835

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlsplit(url)
    domain = parsed_url.netloc
    return domain.endswith("gmail") or domain.endswith("yahoo") or domain.e[8D[K
domain.endswith("hotmail")

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Blocked phishing URL: " + url)
    else:
        print("Allowed safe URL: " + url)

if __name__ == "__main__":
    mitigate_phishing_attack("https://www.example.com")
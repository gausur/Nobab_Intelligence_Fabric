#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-29 20:02:28.221334

import re
import urllib.request

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if not parsed_url.scheme.startswith("http"):
        return False
    if not domain.endswith(".com"):
        return False
    if not re.match(r"^[a-zA-Z0-9.-]+$", domain):
        return False
    return True

def mitigate_phishing_attack(url):
    if not is_phishing_url(url):
        return
    print("Phishing attack detected!")
    return

def main():
    url = input("Enter URL: ")
    mitigate_phishing_attack(url)

if __name__ == "__main__":
    main()
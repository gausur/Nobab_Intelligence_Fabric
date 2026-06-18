#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-18 10:10:39.687493

import re
from urllib.parse import urlparse

def is_phishing_attack(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    if "@" in domain:
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_attack(url):
        print("Possible phishing attack detected!")
        exit()
    else:
        pass

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing_attack(url)
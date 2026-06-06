#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-06 21:00:06.596435

import re
from urllib import parse

def is_phishing_attack(url):
    parsed_url = parse.urlparse(url)
    hostname = parsed_url.netloc
    if not hostname:
        return False
    if "http" in hostname:
        return False
    if ".com" in hostname or ".org" in hostname or ".edu" in hostname:
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    parsed_url = parse.urlparse(url)
    hostname = parsed_url.netloc
    if is_phishing_attack(hostname):
        print("This is a phishing attack!")
    else:
        print("This is not a phishing attack.")

if __name__ == "__main__":
    mitigate_phishing_attack("https://www.example.com")
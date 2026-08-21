#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-21 19:21:25.953454

import re
import requests
from urllib.parse import urlparse

def is_phishing_attempt(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if re.search(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        return False
    return True

def mitigate_phishing_attempt(url):
    if is_phishing_attempt(url):
        print("Possible phishing attempt detected!")
        return True
    return False

def main():
    url = input("Enter a URL: ")
    mitigate_phishing_attempt(url)

if __name__ == "__main__":
    main()
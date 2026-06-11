#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-11 00:13:47.359028

import re
import requests
from urllib.parse import urlparse

def is_phishing_site(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == "example.com":
        return True
    else:
        return False

def mitigate_phishing_attack():
    print("This is a phishing attack!")

def main():
    url = input("Enter URL: ")
    if is_phishing_site(url):
        mitigate_phishing_attack()
    else:
        print("Not a phishing site.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-24 14:34:45.083906

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme == "http" or parsed_url.scheme == "https":
        domain = parsed_url.netloc
        if domain.endswith("google.com"):
            return True
        elif domain.endswith("facebook.com"):
            return True
        elif domain.endswith("yahoo.com"):
            return True
        else:
            return False
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

def main():
    url = input("Enter URL: ")
    mitigate_phishing_attack(url)

if __name__ == "__main__":
    main()
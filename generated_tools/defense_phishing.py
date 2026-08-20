#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 05:25:45.187365

import re
import urllib.parse

def detect_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith(".com"):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith(".com"):
        return url.replace(domain, "example.com")
    else:
        return url

def main():
    url = input("Enter a URL: ")
    if detect_phishing_attack(url):
        print("Phishing attack detected!")
        mitigated_url = mitigate_phishing_attack(url)
        print("Mitigated URL:", mitigated_url)
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()
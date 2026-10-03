#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-03 21:59:51.164891

import re
import urllib.parse

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith(".com") or domain.endswith(".org"):
        return True
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")

def main():
    url = "https://www.example.com"
    mitigate_phishing(url)

if __name__ == "__main__":
    main()
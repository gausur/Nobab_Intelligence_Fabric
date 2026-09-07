#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-07 00:36:30.027909

import re
import urllib.parse

def detect_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme != "https":
        return False
    if parsed_url.netloc.endswith("gmail.com"):
        return True
    return False

def mitigate_phishing_attack(url):
    if detect_phishing_attack(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attack("http://example.com")
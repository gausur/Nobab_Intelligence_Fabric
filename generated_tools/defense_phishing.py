#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 11:20:13.402381

import re

def detect_phishing(url):
    pattern = r"^https?://[a-zA-Z0-9.-]+(:[0-9]+)?$"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Phishing attack detected!")
    else:
        print("Not a phishing attack.")

if __name__ == "__main__":
    url = input("Enter a URL: ")
    mitigate_phishing(url)
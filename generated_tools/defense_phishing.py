#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-18 23:47:35.217552

import re

def is_phishing(url):
    pattern = r"^https://([a-z0-9.-]+)\.([a-z]{2,3}(\.[a-z]{2})?)/$"
    match = re.match(pattern, url)
    if match:
        domain = match.group(1)
        tld = match.group(2)
        if tld in ["com", "org", "net"]:
            return True
    return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attempt detected!")
        return False
    else:
        return True

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-07 23:01:06.637357

import re
from urllib.parse import urlparse

def is_phishing_attempt(url):
    parsed = urlparse(url)
    if not parsed.hostname:
        return False
    hostname = parsed.hostname.lower()
    if hostname.endswith(".onion") or hostname.endswith(".i2p"):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_attempt(url):
        print("Possible phishing attempt detected!")
        input("Please proceed with caution.")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    mitigate_phishing_attack(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-14 19:40:05.706212

import re

def is_phishing_attempt(url):
    pattern = r"[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$"
    if re.match(pattern, url):
        return False
    else:
        return True

def mitigate_phishing_attempt(url):
    if is_phishing_attempt(url):
        print("Possible phishing attempt detected. Aborting...")
        exit(1)

if __name__ == "__main__":
    mitigate_phishing_attempt(input("Enter URL: "))
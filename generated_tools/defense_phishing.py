#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-09 14:35:21.495505

import re

def is_phishing_url(url):
    return re.match(r"https?://[^/]*\.(?:porn|xxx)", url)

def mitigate_phishing_attack():
    print("Phishing attack detected!")

if __name__ == "__main__":
    url = input("Enter URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack()
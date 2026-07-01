#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-01 04:17:27.229898

import re

def is_phishing(url):
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}(/\S*)?$"
    if not re.match(pattern, url):
        return False
    else:
        return True

def mitigate_phishing(url):
    # Implement your mitigation strategy here
    pass

if __name__ == "__main__":
    url = input("Enter URL: ")
    if is_phishing(url):
        mitigate_phishing(url)
    else:
        print("URL is not a phishing site.")
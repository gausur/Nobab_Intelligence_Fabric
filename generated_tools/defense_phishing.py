#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-14 03:40:25.977996

import re

def is_phishing_url(url):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack():
    # implement mitigation strategy
    pass

while True:
    url = input("Enter URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack()
    else:
        print("URL is not a phishing site.")
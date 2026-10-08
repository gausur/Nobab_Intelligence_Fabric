#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-08 00:40:40.669344

import requests
import re

def is_phishing_site(url):
    response = requests.get(url)
    html = response.text
    if re.search(r'<title>.*<\/title>', html):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_site(url):
        print("Phishing site detected!")
        return
    else:
        print("No phishing site detected.")
        return

mitigate_phishing_attack(input("Enter URL: "))
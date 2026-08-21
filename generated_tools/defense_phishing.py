#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-21 22:20:13.978771

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    host = parsed_url.netloc
    if host.endswith('.gov') or host.endswith('.mil'):
        return False
    else:
        return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        return
    else:
        print("No phishing attack detected.")

url = input("Enter a URL: ")
mitigate_phishing_attack(url)
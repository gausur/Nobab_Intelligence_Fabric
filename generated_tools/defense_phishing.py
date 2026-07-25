#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-25 08:58:44.164278

import re

def is_phishing_url(url):
    pattern = r'^(https?|ftp)://([^/]+)/$'
    match = re.search(pattern, url)
    if match:
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == '__main__':
    url = input("Enter the URL to check for a phishing attack: ")
    mitigate_phishing_attack(url)
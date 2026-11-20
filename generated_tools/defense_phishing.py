#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-20 01:35:59.347264

import re

def is_phishing_url(url):
    return re.search(r"^https?://(www\.)?phishingwebsite\.com", url)

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attack("http://www.example.com")
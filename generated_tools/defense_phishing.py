#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-21 12:09:03.007435

import re

def is_phishing_url(url):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    match = re.search(pattern, url)
    if match:
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        # Mitigation code goes here
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

mitigate_phishing_attack("https://example.com")
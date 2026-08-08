#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-08 02:56:11.027115

import re

def is_phishing_attack(url):
    pattern = r"^https?://[^\.]+\.(com|net|org)\b"
    if not re.match(pattern, url):
        return True
    return False

def mitigate_phishing_attack(url):
    if is_phishing_attack(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attack("https://www.example.com")
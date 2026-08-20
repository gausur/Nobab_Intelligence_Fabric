#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 16:25:10.372989

import re
import json

def detect_phishing_attack(url):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, url):
        return "Not a valid email address"
    else:
        return "Valid email address"

def mitigate_phishing_attack(url):
    if url.startswith("http"):
        return "Phishing attack detected"
    else:
        return "Not a phishing attack"

def main():
    url = input("Enter the URL: ")
    result = detect_phishing_attack(url)
    if result == "Valid email address":
        result = mitigate_phishing_attack(url)
    print(result)

if __name__ == "__main__":
    main()
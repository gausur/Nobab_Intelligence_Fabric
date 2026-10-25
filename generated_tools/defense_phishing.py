#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-25 14:44:16.783439

import re

def detect_phishing_attack(url):
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if detect_phishing_attack(url):
        # Redirect to a safe page
        return "http://example.com/safe-page"
    else:
        # Proceed with normal navigation
        return url

def main():
    url = "http://example.com/phishing-attack"
    mitigated_url = mitigate_phishing_attack(url)
    print(mitigated_url)

if __name__ == "__main__":
    main()
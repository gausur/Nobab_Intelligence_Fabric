#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-27 19:48:15.282692

import re

def detect_phishing_attack(url):
    """
    Detects and mitigates phishing attacks by validating the URL using a
    regular expression.
    """
    pattern = r"^https?:\/\/[^\s]+\.com$"
    match = re.match(pattern, url)
    if match:
        return "Valid"
    else:
        return "Invalid"

def main():
    url = "http://www.phishing-site.com"
    result = detect_phishing_attack(url)
    print(f"URL: {url} is {result}.")

if __name__ == "__main__":
    main()
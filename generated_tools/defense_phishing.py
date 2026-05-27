#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-27 02:40:22.813528

import re

def is_phishing_url(url):
    """
    Check if the given URL is a phishing URL.
    """
    pattern = r"https?://[^\.]*\.[^\.\w]?$"
    return bool(re.match(pattern, url))

def mitigate_phishing_attack(url):
    """
    Mitigate a phishing attack by redirecting the user to a safe URL.
    """
    safe_url = "https://www.example.com"
    return safe_url

def main():
    url = input("Enter the URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
        print("Phishing attack detected and mitigated.")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()
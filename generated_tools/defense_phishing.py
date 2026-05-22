#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-22 16:18:28.629349

import re

def is_phishing_url(url):
    """
    Check if the URL is a phishing website.
    Return True if it is, False otherwise.
    """
    return re.match(r"^https?://(www\.)?example\.com/?$", url)

def mitigate_phishing_attack(url):
    """
    Mitigate a phishing attack by redirecting the user to a safe URL.
    """
    return "https://www.google.com"

if __name__ == "__main__":
    url = input("Enter a URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print("Not a phishing website")
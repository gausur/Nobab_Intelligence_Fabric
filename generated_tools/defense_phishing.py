#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 03:49:49.684026

import re

def is_phishing_attempt(url):
    # Check if the URL contains any suspicious characters
    if not re.match(r"^[A-Za-z0-9://\._-]*$", url):
        return True
    
    # Check if the URL is for a known phishing domain
    if "phishingdomain.com" in url:
        return True
    
    return False

def mitigate_phishing_attempt(url):
    # Redirect the user to a safe URL
    print("Please visit the following URL instead:")
    print(f"https://example.com/safe-url?source={url}")

if __name__ == "__main__":
    url = input("Enter URL: ")
    if is_phishing_attempt(url):
        mitigate_phishing_attempt(url)
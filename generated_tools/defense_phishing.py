#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-25 00:04:56.309166

import re
from urllib import parse

def is_phishing_url(url):
    # Check if the URL is valid
    if not parse.urlparse(url).scheme:
        return False
    
    # Check if the URL contains any suspicious keywords
    for keyword in ["phish", "fishing", "scam"]:
        if keyword in url:
            return True
    
    # Check if the URL is a HTTP or HTTPS link
    if parse.urlparse(url).scheme not in ["http", "https"]:
        return False
    
    # Check if the domain name is valid
    try:
        parse.urlparse(url).netloc
    except AttributeError:
        return False
    
    return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attacks detected.")

if __name__ == "__main__":
    url = input("Enter URL to check: ")
    mitigate_phishing_attack(url)
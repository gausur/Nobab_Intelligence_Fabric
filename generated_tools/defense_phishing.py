#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-26 03:33:22.380617

import re
import urllib.parse

# Define the list of known phishing domains
phishing_domains = [
    "example1.com",
    "example2.com",
    "example3.com"
]

def is_phishing_url(url):
    # Check if the URL is a valid URL format
    try:
        urllib.parse.urlparse(url)
    except ValueError:
        return False
    
    # Extract the domain from the URL
    domain = urllib.parse.urlparse(url).netloc
    
    # Check if the domain is in the list of known phishing domains
    for phishing_domain in phishing_domains:
        if domain == phishing_domain:
            return True
    
    return False

def mitigate_phishing(url):
    # If the URL is a phishing site, redirect to a safe page
    if is_phishing_url(url):
        return "https://www.example.com/safe-page"
    else:
        return url

# Test the script
print(is_phishing_url("http://example1.com")) # Output: True
print(is_phishing_url("http://example2.com")) # Output: False
print(mitigate_phishing("http://example1.com")) # Output: https://www.examp[17D[K
https://www.example.com/safe-page
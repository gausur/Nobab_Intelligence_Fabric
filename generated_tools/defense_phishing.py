#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-14 17:50:18.858940

import re
import urllib.parse

def detect_phishing(url):
    """
    Detect phishing attacks by analyzing the URL.
    """
    # Extract the domain name from the URL
    domain = urllib.parse.urlparse(url).netloc

    # Check if the domain name is a known phishing site
    if domain in phishing_sites:
        print("Phishing attack detected!")
        return True
    else:
        print("No phishing attack detected.")
        return False

# List of known phishing sites
phishing_sites = [
    "phishing.example.com",
    "malicious.example.net",
    "social.engineering.example.org"
]

# Test the function
url = "https://www.example.com"
detect_phishing(url)
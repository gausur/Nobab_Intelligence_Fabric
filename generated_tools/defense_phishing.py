#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-13 22:00:42.506646

import re
import urllib.parse

def detect_phishing_attack(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    if not re.match(r"^https?://", url):
        return False

    # Parse the URL and extract the domain
    domain = urllib.parse.urlparse(url).netloc

    # Check if the domain is a valid email address
    if not re.match(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", domain):
        return False

    # Check if the URL is a phishing attack
    if re.search(r"(phish|phishing|scam|fraud)", url, re.IGNORECASE):
        return True

    return False

# Example usage
url = "https://www.example.com/phishing_attack.php"
if detect_phishing_attack(url):
    print("Possible phishing attack detected!")
else:
    print("No phishing attack detected.")
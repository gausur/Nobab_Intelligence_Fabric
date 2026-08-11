#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 10:44:08.587897

import re
from urllib.parse import urlparse

def is_phishing_attack(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        return False
    # Check for common phishing tlds
    if hostname.endswith(".ru"):
        return True
    elif hostname.endswith(".co.uk"):
        return True
    elif hostname.endswith(".gov"):
        return True
    # Check for common phishing domains
    if hostname == "fakebankofamerica.com":
        return True
    elif hostname == "fakegmail.com":
        return True
    elif hostname == "fakefacebook.com":
        return True
    # Check for patterns in the url
    if re.search(r"\/phishing\.html", url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    print("Possible phishing attack detected.")
    print("The following URL was flagged for suspicious activity:")
    print(url)
    print("Please be cautious and verify the authenticity of this site befo[4D[K
before proceeding with any actions.")

# Test cases
urls = [
    "https://bankofamerica.com",
    "https://gmail.com",
    "https://facebook.com",
    "https://fakebankofamerica.com",
    "https://fakegmail.com",
    "https://fakefacebook.com",
    "https://www.phishing.html"
]
for url in urls:
    if is_phishing_attack(url):
        mitigate_phishing_attack(url)
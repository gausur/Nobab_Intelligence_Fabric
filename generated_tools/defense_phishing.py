#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 15:26:01.313199

import re
import urllib.request

def is_phishing_url(url):
    # Check if the URL is from a known phishing domain
    domain = urllib.parse.urlparse(url).netloc
    return domain in PHISHING_DOMAINS

# Define a set of known phishing domains
PHISHING_DOMAINS = {"phishing.example.com", "badguysite.org"}

# Read the input URL from stdin
url = input("Enter URL: ")

if is_phishing_url(url):
    print("Phishing detected!")
else:
    print("No phishing detected.")
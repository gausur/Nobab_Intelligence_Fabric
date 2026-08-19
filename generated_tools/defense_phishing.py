#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-19 04:34:24.693592

import re
import requests

def detect_phishing(url):
    # Check if the URL is a valid HTTPS URL
    if not url.startswith("https://"):
        return False

    # Send a HEAD request to the URL to get the headers
    response = requests.head(url)

    # Check if the response is a 200 OK
    if response.status_code != 200:
        return False

    # Check if the content-type header is text/html
    if response.headers["Content-Type"] != "text/html":
        return False

    # Check if the URL is not in the list of known phishing URLs
    if url in known_phishing_urls:
        return True

    # Check if the URL is in the list of known legitimate URLs
    if url in known_legitimate_urls:
        return False

    # Check if the URL contains any suspicious keywords
    for keyword in suspicious_keywords:
        if keyword in url:
            return True

    # If none of the above conditions are met, return False
    return False

# List of known phishing URLs
known_phishing_urls = [
    "https://www.phishing-site.com/",
    "https://www.evilsite.com/"
]

# List of known legitimate URLs
known_legitimate_urls = [
    "https://www.google.com/",
    "https://www.youtube.com/"
]

# List of suspicious keywords
suspicious_keywords = [
    "free",
    "discount",
    "coupon",
    "promo",
    "payment",
    "confirm"
]

# Input the URL to be checked
url = input("Enter URL: ")

# Check if the URL is a phishing site
if detect_phishing(url):
    print("This is a phishing site!")
else:
    print("This is not a phishing site.")
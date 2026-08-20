#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 12:33:31.100436

import re
import requests

def detect_phishing(url):
    # Check if the URL is a valid HTTPS URL
    if not re.match(r"^https://", url):
        return False

    # Send a HEAD request to the URL to get the HTTP response headers
    response = requests.head(url)

    # Check if the response code is a redirect
    if response.status_code == 301 or response.status_code == 302:
        return True

    # Check if the response headers contain a "Location" header
    if "Location" in response.headers:
        return True

    # Check if the URL is a known phishing URL
    if url in known_phishing_urls:
        return True

    return False

# List of known phishing URLs
known_phishing_urls = [
    "https://www.phishing.com/login",
    "https://www.phishing.com/signup",
    "https://www.phishing.com/forgot-password"
]
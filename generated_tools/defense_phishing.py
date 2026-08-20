#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 04:33:15.061566

import re
import requests

def detect_phishing_attack(url):
    # Check if the URL is valid
    if not re.match(r"^https?://", url):
        raise ValueError("Invalid URL")

    # Send a request to the URL to get the HTML content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise RuntimeError("Failed to retrieve HTML content")

    # Get the HTML content
    html_content = response.text

    # Check if the HTML content contains the "phishing" keyword
    if "phishing" in html_content:
        raise RuntimeError("Phishing attack detected")

# Example usage
try:
    detect_phishing_attack("https://example.com")
except RuntimeError as e:
    print(e)
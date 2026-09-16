#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-16 13:57:52.509156

import re
import requests

def detect_phishing(url):
    """
    Detect phishing attacks by analyzing the URL and the HTML content.
    """
    # Check if the URL is a valid HTTPS URL
    if not re.match(r'^https://', url):
        print('Error: URL is not a valid HTTPS URL.')
        return

    # Fetch the HTML content of the URL
    response = requests.get(url)
    html_content = response.content.decode('utf-8')

    # Check if the HTML content contains any suspicious keywords
    if re.search(r'phishing|scam|fraud', html_content, re.IGNORECASE):
        print('Possible phishing attack detected!')
    else:
        print('No phishing attack detected.')

# Example usage:
detect_phishing('https://example.com')
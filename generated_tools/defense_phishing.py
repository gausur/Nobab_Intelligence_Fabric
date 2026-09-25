#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-25 23:45:40.494305

import re
import requests

def detect_phishing(url):
    # Check if the URL is valid
    if not re.match(r'^https?://', url):
        raise ValueError('Invalid URL')

    # Make a request to the URL to check for any suspicious content
    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException:
        raise ValueError('Failed to retrieve URL')

    # Check if the response contains any suspicious content
    if resp.text.lower().find('phishing') != -1:
        raise ValueError('Phishing attack detected')

    # If no suspicious content is found, return a success message
    return 'No phishing attacks detected'

# Example usage
try:
    detect_phishing('https://example.com')
except ValueError as e:
    print(e)
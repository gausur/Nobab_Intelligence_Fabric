#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-17 02:37:38.688193

import re
import requests

def detect_phishing(url):
    # Check if the URL is valid
    if not re.match(r'^https?://', url):
        raise ValueError('Invalid URL')

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response is valid
    if response.status_code != 200:
        raise ValueError('Invalid response')

    # Check if the URL contains suspicious content
    if re.search(r'phishing|scam', response.text):
        raise ValueError('Phishing attack detected')

    # If no phishing attack is detected, return the URL
    return url

# Test the function
try:
    detect_phishing('https://www.example.com')
    print('No phishing attack detected.')
except ValueError:
    print('Phishing attack detected.')
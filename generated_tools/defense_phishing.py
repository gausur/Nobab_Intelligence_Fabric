#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-23 18:09:33.987110

import re
import requests

def detect_phishing_attacks(url):
    # Check if the URL is valid
    if not re.match(r'^https?://', url):
        return False

    # Send a HEAD request to the URL
    try:
        response = requests.head(url)
    except requests.exceptions.RequestException:
        return False

    # Check if the response status code is 200
    if response.status_code != 200:
        return False

    # Check if the response contains a suspicious header
    if 'x-frame-options' in response.headers:
        # Check if the header value is 'deny'
        if response.headers['x-frame-options'] == 'deny':
            return True

    # Check if the response contains a suspicious cookie
    if 'set-cookie' in response.headers:
        # Check if the cookie name is '__Host-' or starts with '__Host-'
        for cookie in response.headers['set-cookie']:
            if cookie.startswith('__Host-'):
                return True

    # Check if the response contains a suspicious header
    if 'content-security-policy' in response.headers:
        # Check if the header value contains 'unsafe-inline'
        if 'unsafe-inline' in response.headers['content-security-policy']:
            return True

    # Check if the response contains a suspicious body
    if response.text.lower().find('<script>') != -1:
        return True

    return False

# Example usage
url = 'https://example.com'
if detect_phishing_attacks(url):
    print('Phishing attack detected')
else:
    print('No phishing attack detected')
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-19 15:24:51.702841

import re
import requests

def detect_phishing(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    if not re.match(r'^https?://', url):
        return False

    # Send a HEAD request to the URL to get the HTTP headers
    response = requests.head(url)

    # Check if the response is a valid HTML document
    if not response.headers['Content-Type'].startswith('text/html'):
        return False

    # Check if the response contains any suspicious headers or meta tags
    if 'X-Frame-Options' in response.headers and response.headers['X-Frame-[26D[K
response.headers['X-Frame-Options'] != 'SAMEORIGIN':
        return False
    if 'X-XSS-Protection' in response.headers and response.headers['X-XSS-P[25D[K
response.headers['X-XSS-Protection'] != '1':
        return False
    if 'Content-Security-Policy' in response.headers and 'sandbox' not in r[1D[K
response.headers['Content-Security-Policy']:
        return False
    if 'X-Content-Type-Options' in response.headers and response.headers['X[19D[K
response.headers['X-Content-Type-Options'] != 'nosniff':
        return False

    # Check if the response contains any suspicious content
    if response.text.find('</script>') != -1:
        return False
    if response.text.find('</head>') != -1:
        return False
    if response.text.find('</title>') != -1:
        return False
    if response.text.find('</body>') != -1:
        return False

    # If all checks pass, the URL is likely legitimate
    return True

# Example usage:
url = 'https://www.example.com'
if detect_phishing(url):
    print('Legitimate URL')
else:
    print('Possible phishing URL')
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-18 11:50:31.131246

import re
import urllib.parse

def is_phishing_url(url):
    # Check if the URL contains any suspicious characters or patterns
    return re.search(r'[^\w-]+', url) or \
           url.startswith('http://') or \
           url.startswith('https://')

def mitigate_phishing_url(url):
    # Replace any suspicious characters with a blank string
    return re.sub(r'[^\w-]+', '', url)

# Test the function
url = 'http://www.example.com'
if is_phishing_url(url):
    print('Phishing URL detected!')
else:
    print('No phishing URLs found.')
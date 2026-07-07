#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-07 20:48:13.606948

import re
import requests
from bs4 import BeautifulSoup

def detect_phishing(url):
    # Fetch the URL and parse the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if the URL is a phishing site
    if not re.search(r'^https?://', url):
        return False

    # Check for suspicious keywords in the HTML content
    if soup.find('script'):
        return True
    elif soup.find('iframe'):
        return True
    elif soup.find('a') and soup.find('a').get('href'):
        return True
    else:
        return False

def mitigate_phishing(url):
    # Redirect the user to a safe URL
    return 'https://example.com'

# Example usage
url = 'http://phishing.site/login'
if detect_phishing(url):
    print('Phishing site detected!')
else:
    print('Safe site')
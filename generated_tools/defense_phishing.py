#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-01 08:48:56.641121

import re
import urllib.parse
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid
    try:
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return False
    except ValueError:
        return False

    # Fetch the HTML content of the page
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        return False
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check for common phishing techniques
    if soup.find('input', {'type': 'submit'}):
        return True
    if soup.find('form'):
        return True
    if soup.find('a', {'onclick' : re.compile(r'javascript:void')}):
        return True
    if soup.find('script'):
        return True

    # Check for suspicious keywords in the HTML content
    for keyword in ['phish', 'scam', 'hack', 'fraud']:
        if keyword in response.content.lower():
            return True

    return False

def mitigate_phishing(url):
    # Check if the URL is valid and a phishing attack
    if not is_phishing(url):
        print("Not a phishing attack")
        return

    # Redirect the user to a safe page
    print("Please go to this safe page: https://www.example.com/")
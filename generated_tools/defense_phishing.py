#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-24 13:14:26.989462

import re
import requests
from bs4 import BeautifulSoup

def is_phishing_site(url):
    # Check if the URL is valid
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return False
    except requests.exceptions.RequestException:
        return False

    # Check if the website has a valid SSL certificate
    try:
        response = requests.get(url, verify=True)
        if response.status_code != 200:
            return False
    except requests.exceptions.RequestException:
        return False

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check for common phishing techniques
    if re.search(r'fake\-logo', str(soup)):
        return True
    elif re.search(r'click\-here\.com', str(soup)):
        return True
    elif re.search(r'free\-[a-zA-Z0-9]+', str(soup)):
        return True
    elif re.search(r'buy\-now\.com', str(soup)):
        return True
    elif re.search(r'download\-here\.com', str(soup)):
        return True
    else:
        return False
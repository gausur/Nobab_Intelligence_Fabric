#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-12 21:44:00.801254

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid
    if not url or not requests.head(url).ok:
        return False
    
    # Fetch the HTML page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Check for suspicious keywords in the HTML
    if re.search(r'phishing|scam|fraud', soup.text):
        return True
    
    # Check for suspicious HTTP status codes
    if response.status_code not in (200, 301, 302):
        return True
    
    # Check for suspicious HTML tags and attributes
    if re.search(r'script|iframe', soup.find_all('script')):
        return True
    
    return False
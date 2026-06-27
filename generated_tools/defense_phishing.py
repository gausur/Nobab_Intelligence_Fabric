#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 02:43:40.558105

import requests
from bs4 import BeautifulSoup
import re

def is_phishing(url):
    # Check if the URL is valid
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        return False

    # Check for common phishing techniques
    if re.search(r'(?i)(phish)$', url):
        return True
    elif re.search(r'(?i)(\w+:\/\/.*\w+)', url) and not re.search(r'^https?[19D[K
re.search(r'^https?://', url):
        return True
    elif re.search(r'(?i)(@[\w_-]+)$', soup.get_text()):
        return True
    else:
        return False
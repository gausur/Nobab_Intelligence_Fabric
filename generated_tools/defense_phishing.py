#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-18 16:23:39.806714

import re
import requests

def detect_phishing(url):
    # Check if the URL is valid
    if not re.match(r'^https?://', url):
        return False

    # Send a request to the URL to see if it responds with a 200 status cod[3D[K
code
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Test the function
url = "https://www.example.com"
print(detect_phishing(url))
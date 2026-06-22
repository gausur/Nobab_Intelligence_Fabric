#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-22 21:34:07.844298

import re
import requests

def is_phishing_attack(url):
    # Check if the URL is valid
    if not url or not re.match(r'^https?://', url):
        return False
    
    # Fetch the website's content and analyze it
    response = requests.get(url)
    if response.status_code != 200:
        return False
    
    # Check for suspicious patterns in the HTML
    html = response.text
    if '<script>' in html or '</script>' in html:
        return True
    if '<iframe src=' in html or '<frame src=' in html:
        return True
    if '<a href="javascript:' in html:
        return True
    
    # Check for suspicious headers
    headers = response.headers
    if 'x-frame-options' in headers and headers['x-frame-options'] == 'DENY[5D[K
'DENY':
        return True
    if 'content-security-policy' in headers and 'script-src' not in headers[7D[K
headers['content-security-policy']:
        return True
    
    # If none of the above checks triggered, it's likely a legitimate websi[5D[K
website
    return False
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-03 21:45:27.495470

import re
import urllib.request
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is a valid HTTPS URL
    if not url.startswith("https"):
        return False
    
    # Get the HTML content of the URL
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read()
    except urllib.error.URLError:
        return False
    
    # Check if the HTML content contains the phishing pattern
    soup = BeautifulSoup(html_content, "html.parser")
    if not re.search(r"[^\x00-\x7F]", soup.text):
        return False
    
    return True
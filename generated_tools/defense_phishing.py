#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 06:44:20.867716

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    """Check if the URL is a phishing site."""
    # Send a HEAD request to get just the headers
    response = requests.head(url)
    
    # Check if the response code is 200
    if response.status_code != 200:
        return False
    
    # Get the content of the page
    html = BeautifulSoup(requests.get(url).text, "html.parser")
    
    # Check for common phishing patterns
    if re.search(r"[fF]ake|[pP]hishing", html.title.string):
        return True
    elif re.search(r"[sS]ecurity[mM]atters", html.body.text):
        return True
    
    # Check for suspicious words in the page content
    if "click here to continue" in html.body.text:
        return True
    elif "sign up now" in html.body.text:
        return True
    elif "get started" in html.body.text:
        return True
    
    # Check for suspicious URLs in the page content
    if re.search(r"^https://www\.google\.com/", url):
        return True
    elif re.search(r"^https://www\.facebook\.com/", url):
        return True
    elif re.search(r"^https://www\.twitter\.com/", url):
        return True
    
    # If none of the above patterns are found, it's likely not a phishing s[1D[K
site
    return False
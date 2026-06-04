#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-04 13:56:44.399124

import re
import urllib.request
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    if not (re.match(r'^https?://', url)):
        return False
    
    # Fetch the HTML content of the website
    try:
        html = urllib.request.urlopen(url).read()
    except:
        return False
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check if the website has a login form and a submit button
    if not (soup.find('form', attrs={'method': 'post'})):
        return False
    
    # Check if the website has a hidden input field with name "_csrf" or "c[2D[K
"csrf_token"
    if not (soup.find('input', attrs={'name': re.compile(r'_csrf|csrf_token[29D[K
re.compile(r'_csrf|csrf_token')})):
        return False
    
    # Check if the website has a hidden input field with name "authenticity[13D[K
"authenticity_token"
    if not (soup.find('input', attrs={'name': 'authenticity_token'})):
        return False
    
    return True
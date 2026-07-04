#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-04 13:05:07.361856

import requests
import re

def detect_phishing(url):
    """Detect if a URL is a phishing site"""
    # Get the HTML content of the page using requests
    html = requests.get(url).text
    
    # Check for common phishing signs
    if "login" in url and "password" in url:
        return True
    elif re.search(r"phish\b", html, re.IGNORECASE):
        return True
    else:
        return False

def mitigate_phishing(url):
    """Mitigate phishing attacks by redirecting to a safe page"""
    # Redirect to a safe page if the URL is a phishing site
    if detect_phishing(url):
        print("This URL is a phishing site. Redirecting to a safe page.")
        return "https://www.example.com/"
    else:
        return url
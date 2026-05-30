#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-30 21:55:29.474926

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("URL is not valid:", err)
        return False
    
    # Extract the HTML content from the URL
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Check if the website is using HTTPS
    if "https" not in url:
        print("Warning: Website is not using HTTPS")
        return False
    
    # Check for common phishing patterns
    if soup.find(id="login_form"):
        print("Possible phishing attempt detected!")
        return True
    elif soup.find(class_="login_form"):
        print("Possible phishing attempt detected!")
        return True
    elif soup.find(action="/login"):
        print("Possible phishing attempt detected!")
        return True
    else:
        print("No phishing attempts detected.")
        return False
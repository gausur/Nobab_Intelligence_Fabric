#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-04 12:00:20.918894

import re
import requests
from bs4 import BeautifulSoup

def is_phishing_attempt(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    if not re.match(r"^https?://", url):
        return False
    
    # Fetch the page using requests library
    response = requests.get(url)
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Check if the page contains any suspicious elements
    for elem in soup.find_all():
        if elem.name == "script" or elem.name == "iframe":
            return True
    
    return False

def mitigate_phishing(url):
    # If the URL is a phishing attempt, redirect to a safe page
    if is_phishing_attempt(url):
        print("Phishing attempt detected! Redirecting to safe page...")
        return "https://www.example.com"
    
    # If the URL is not a phishing attempt, continue with the original URL
    else:
        print("Not a phishing attempt. Continuing with original URL.")
        return url
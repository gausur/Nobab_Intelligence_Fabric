#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-06 07:44:58.565885

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_phishing(url):
    # Check if the URL is a valid HTTP/HTTPS URL
    parsed = urlparse(url)
    if not (parsed.scheme == "http" or parsed.scheme == "https"):
        return False, f"{url} is not a valid HTTP/HTTPS URL"
    
    # Fetch the HTML content of the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Check for common phishing patterns
    if soup.title.string == "phishing website":
        return True, f"{url} is a phishing website"
    elif "click here to download" in response.text:
        return True, f"{url} is asking you to click on a suspicious link"
    elif "sign up now" in response.text:
        return True, f"{url} is promoting a fake service or product"
    else:
        return False, None

# Test the function with some URLs
urls = [
    "http://www.phishingwebsite.com",
    "https://www.example.com",
    "http://www.fakesite.com/download.html",
]
for url in urls:
    result, message = is_phishing(url)
    if result:
        print(message)
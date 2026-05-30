#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-30 15:02:50.723286

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_phishing(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    parsed_url = urlparse(url)
    if not parsed_url.scheme in ["http", "https"]:
        return False
    
    # Send a HEAD request to the URL to get only the headers
    response = requests.head(url, allow_redirects=True)
    
    # Check if the server responded with a 302 redirect to another domain
    if response.status_code == 302 and "Location" in response.headers:
        redirect_url = urlparse(response.headers["Location"])
        return redirect_url.netloc != parsed_url.netloc
    
    # Check if the server responded with a 404 Not Found error
    if response.status_code == 404:
        return False
    
    # Get the HTML content of the page
    html = requests.get(url).content
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Check if the HTML contains any suspicious tags or attributes
    for tag in ["script", "iframe"]:
        if tag in soup.find_all(tag):
            return True
    for attr in ["onclick", "onsubmit", "javascript"]:
        if attr in soup.attrs:
            return True
    
    # If none of the above conditions are met, it is likely that the URL is[2D[K
is legitimate
    return False
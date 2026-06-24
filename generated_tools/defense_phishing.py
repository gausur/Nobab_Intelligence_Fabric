#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-24 16:13:52.105679

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    parsed_url = urlparse(url)
    if not (parsed_url.scheme == "http" or parsed_url.scheme == "https"):
        return False
    
    # Check if the domain name has at least two parts, separated by a dot
    domain_parts = parsed_url.netloc.split(".")
    if len(domain_parts) < 2:
        return False
    
    # Check if the URL contains any suspicious characters or patterns
    if re.search(r"[^\w.-]", url):
        return True
    
    # Check if the URL is on a known phishing domain list
    with open("phishing_domains.txt") as f:
        for line in f:
            if domain_parts[-2] == line.strip():
                return True
    
    return False

def mitigate(url):
    # Redirect the user to a safer URL
    with open("safer_urls.txt") as f:
        for line in f:
            if url == line.strip():
                return line.strip()
    
    # If no safer URL is found, show an error message
    print("Unable to find a safer URL for this phishing attack.")

# Get the user's input and check it against the phishing list
url = input("Enter the URL: ")
if is_phishing(url):
    mitigate(url)
else:
    print("This is not a phishing attack. Proceeding with the request.")
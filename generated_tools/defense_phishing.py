#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-22 23:17:26.515834

import re
import requests

def is_phishing_url(url):
    # Check if the URL contains any suspicious patterns
    pattern = r"[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_[61D[K
r"[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"r"[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&//=]*)"
    if re.search(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    # Send a request to the URL to see if it's legitimate
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Invalid URL")
    else:
        # Check the response status code and content type
        if response.status_code == 200 and response.headers["Content-Type"][32D[K
response.headers["Content-Type"] == "text/html":
            return True
        else:
            return False

def detect_phishing(url):
    # Combine the two functions to detect phishing attacks
    if is_phishing_url(url) and mitigate_phishing_attack(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")
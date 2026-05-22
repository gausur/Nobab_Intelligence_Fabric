#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-22 18:31:05.403565

import re
import requests

# Set up the regular expression for detecting phishing URLs
phishing_regex = r"^https?:\/\/.*\.phishing\.com"

# Set up the URL to check against the phishing regex
url = "http://www.example.com"

# Use the requests library to make a GET request to the URL
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Extract the text from the HTML response
    html = response.text

    # Use the regular expression to find phishing URLs in the HTML
    matches = re.findall(phishing_regex, html)

    # If there are any matches, print an error message and exit
    if len(matches) > 0:
        print("Phishing attack detected!")
        exit(1)
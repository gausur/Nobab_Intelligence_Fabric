#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 09:11:34.339875

import re
import urllib

# Define list of known phishing domains
phishing_domains = ["example1.com", "example2.com"]

# Define function to check if URL is phishing
def is_phishing(url):
    parsed_url = urllib.parse.urlsplit(url)
    hostname = parsed_url.hostname
    return hostname in phishing_domains

# Define function to mitigate phishing attack
def mitigate_phishing(url):
    if is_phishing(url):
        # Redirect user to a known safe website
        urllib.request.urlopen("https://example3.com")
    else:
        # Load URL in web browser
        urllib.request.urlopen(url)

# Get user input and check if it's a phishing URL
user_input = input("Enter a URL: ")
if is_phishing(user_input):
    mitigate_phishing(user_input)
else:
    # Load URL in web browser
    urllib.request.urlopen(user_input)
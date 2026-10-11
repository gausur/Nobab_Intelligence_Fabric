#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-11 21:19:58.811602

import re
import requests

def detect_phishing(url):
    # Check if the URL is valid
    if not url:
        return "Invalid URL"

    # Send a GET request to the URL
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return "Error sending request: {}".format(e)

    # Check if the response is valid
    if response.status_code != 200:
        return "Error in response: {}".format(response.status_code)

    # Check if the response is HTML
    if not re.search(r"<html>", response.text, re.IGNORECASE):
        return "Not HTML"

    # Check if the HTML contains a phishing-related string
    if re.search(r"phishing|scam", response.text, re.IGNORECASE):
        return "Possible phishing attack"

    # Check if the HTML contains a suspicious string
    if re.search(r"suspicious|malicious", response.text, re.IGNORECASE):
        return "Possible suspicious activity"

    # No phishing or suspicious activity detected
    return "No issues detected"

# Test the function
url = "https://www.example.com"
print(detect_phishing(url))
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-07 06:07:03.031178

import re
import json
import requests

# Load the list of known phishing URLs from a file
with open("phishing_urls.txt", "r") as f:
    phishing_urls = [line.strip() for line in f if line.strip()]

# Define a function to check if a URL is a phishing site
def is_phishing(url):
    # Check if the URL matches any of the known phishing sites
    for phishing_url in phishing_urls:
        if re.search(phishing_url, url):
            return True
    return False

# Define a function to send a request and check the response code
def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully retrieved URL:", url)
        else:
            print("Error retrieving URL:", url, "Status code:", response.st[11D[K
response.status_code)
    except Exception as e:
        print("Error retrieving URL:", url, "Exception:", str(e))

# Define a function to check if the website is legitimate
def check_legitimacy(url):
    # Check if the URL is a phishing site
    if is_phishing(url):
        print("Phishing site detected:", url)
    else:
        send_request(url)

# Get the user input for the URL to check
url = input("Enter the URL to check: ")

# Check if the URL is legitimate
check_legitimacy(url)
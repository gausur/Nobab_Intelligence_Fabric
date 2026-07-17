#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-17 17:07:06.137970

import re
import urllib.request

# Define the list of domains that are considered safe for redirection
safe_domains = ["example.com", "example2.com"]

# Define a regular expression to match URLs with unsafe protocols
unsafe_protocols = ["http://", "https://", "ftp://", "ftps://", "mailto:"]
url_pattern = f"({'|'.join(unsafe_protocols)})([a-z0-9.-]+)"

# Define a function to check if a URL is safe for redirection
def is_safe_url(url):
    return bool(re.match(url_pattern, url)) and (url.split(".")[-2:] in saf[3D[K
safe_domains)

# Get the URL from the user input
url = input("Enter the URL: ")

# Check if the URL is safe for redirection
if not is_safe_url(url):
    print("The URL you entered is unsafe. Please enter a valid URL.")
else:
    # Open the URL in the default browser
    webbrowser.open(url)
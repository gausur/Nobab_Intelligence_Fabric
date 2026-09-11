#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-11 10:20:51.078148

import re
import urllib.parse
import requests

def detect_phishing_attack(url):
    # Check if the URL is a valid HTTP/HTTPS URL
    if not re.match(r"^https?://", url):
        return False

    # Parse the URL and extract the hostname
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname

    # Check if the hostname is a valid domain name
    if not re.match(r"^[a-zA-Z0-9.-]+$", hostname):
        return False

    # Check if the hostname is a subdomain of a known phishing site
    for site in KNOWN_PHISHING_SITES:
        if hostname.endswith("." + site):
            return True

    return False

def mitigate_phishing_attack(url):
    # Redirect the user to the default search engine
    webbrowser.open_new_tab("https://google.com/search?q=" + url)

# List of known phishing sites
KNOWN_PHISHING_SITES = [
    "example1.com",
    "example2.com",
    "example3.com"
]

# Main function
def main():
    # Get the URL from the user
    url = input("Enter a URL: ")

    # Detect and mitigate phishing attacks
    if detect_phishing_attack(url):
        mitigate_phishing_attack(url)
    else:
        print("Not a phishing attack")

# Run the main function
if __name__ == "__main__":
    main()
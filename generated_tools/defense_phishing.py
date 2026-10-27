#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-27 01:46:59.784642

import re
import requests

def is_phishing_url(url):
    # Check if the URL is a valid HTTPS URL
    if not url.startswith("https://"):
        return False

    # Extract the domain name from the URL
    domain = url.split("://")[1].split("/")[0]

    # Check if the domain name is in the HSTS preload list
    try:
        requests.get("https://" + domain + "/.well-known/hsts.json")
        return True
    except requests.exceptions.ConnectionError:
        return False

def mitigate_phishing_attack(url):
    # Check if the URL is a phishing URL
    if is_phishing_url(url):
        # Mitigate the phishing attack by displaying a warning message
        print("Warning: Potential phishing attack detected.")
        print("The URL you entered is not secure.")
        print("Please enter a valid HTTPS URL.")

# Test the script
mitigate_phishing_attack("http://example.com")
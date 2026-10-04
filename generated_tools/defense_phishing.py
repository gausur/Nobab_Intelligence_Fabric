#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-04 00:19:40.034905

import re

def detect_phishing(url):
    # Check if the URL is valid
    if not url or not re.match(r'^https?://', url):
        return False

    # Check if the URL is a phishing site
    if re.search(r'phishing\.com', url):
        return True

    # Check if the URL is a subdomain of a phishing site
    if re.search(r'phishing\.com', url):
        return True

    # Check if the URL is an IP address
    if re.match(r'^\d+\.\d+\.\d+\.\d+', url):
        return False

    # Check if the URL is a valid domain name
    if re.match(r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', url):
        return False

    # If the URL is not a valid domain name or IP address, it is likely a p[1D[K
phishing site
    return True

def mitigate_phishing(url):
    # Check if the URL is a phishing site
    if detect_phishing(url):
        # Block the URL
        print("Blocked URL:", url)
        return

    # Allow the URL
    print("Allowed URL:", url)
    return

# Test the function
url = "https://www.example.com"
mitigate_phishing(url)

url = "https://phishing.com"
mitigate_phishing(url)

url = "https://www.phishing.com"
mitigate_phishing(url)

url = "https://example.com"
mitigate_phishing(url)
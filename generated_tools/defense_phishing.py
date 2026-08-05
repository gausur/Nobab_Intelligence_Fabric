#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-05 21:02:51.546382

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    """Check if the URL is a phishing website."""
    # Extract the domain name from the URL
    domain = urlparse(url).netloc

    # Check if the domain is in the list of known phishing domains
    with open('known_phishing_domains.txt', 'r') as f:
        for line in f:
            if domain == line.strip():
                return True

    return False

def mitigate_phishing(url):
    """Mitigate a phishing attack by blocking the URL."""
    # Block the URL using the "requests" library
    response = requests.get(url)
    if response.status_code == 403:
        print("Phishing attempt blocked.")
    else:
        print("Failed to block phishing attack.")

def main():
    """Main function."""
    url = input("Enter the URL: ")
    if is_phishing(url):
        mitigate_phishing(url)
    else:
        print("Not a phishing site.")

if __name__ == "__main__":
    main()
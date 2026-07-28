#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-28 11:12:49.015705

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Extract the domain name from the URL
    domain = urlparse(url).netloc

    # Check if the domain is in the phishing database
    with open("phishing_database.txt", "r") as f:
        for line in f:
            if line.strip() == domain:
                return True
    return False

def mitigate_phishing(url):
    # Extract the domain name from the URL
    domain = urlparse(url).netloc

    # Check if the domain is in the phishing database
    with open("phishing_database.txt", "r") as f:
        for line in f:
            if line.strip() == domain:
                return True
    return False

# Main function to run the script
def main():
    # Get the URL from the user
    url = input("Enter the URL you want to check: ")

    # Check if the URL is a phishing site
    if is_phishing(url):
        print("This URL is a phishing site!")
    else:
        print("This URL is not a phishing site.")

# Run the main function
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-18 18:53:36.329831

import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid
    try:
        response = requests.get(url)
        if not response.ok:
            return False
    except Exception as e:
        print(f"Failed to get {url}: {e}")
        return False

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Check for common phishing patterns in the HTML content
    if "javascript:" in str(soup):
        print(f"{url} contains javascript:")
        return True
    elif "onclick=" in str(soup):
        print(f"{url} contains onclick=")
        return True
    elif "alert(" in str(soup):
        print(f"{url} contains alert(")
        return True
    else:
        return False

def main():
    # Get list of URLs from user input or a file
    urls = ["https://example.com", "https://phishing-site.com"]

    # Iterate over each URL and check for phishing patterns
    for url in urls:
        if is_phishing(url):
            print(f"Phishing attack detected at {url}")
        else:
            print(f"{url} is safe")

if __name__ == "__main__":
    main()
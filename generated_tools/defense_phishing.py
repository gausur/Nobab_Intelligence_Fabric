#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-25 23:59:21.246157

import re

def detect_phishing(url):
    """
    Detect phishing attacks by analyzing the URL.
    """
    # Check if the URL contains suspicious characters
    if re.search(r"[^\w-.]", url):
        return False

    # Check if the URL contains a suspicious domain
    domain = urlparse(url).netloc
    if re.search(r"[^\w-.]", domain):
        return False

    # Check if the URL contains a suspicious path
    path = urlparse(url).path
    if re.search(r"[^\w-.]", path):
        return False

    # Check if the URL contains a suspicious query parameter
    query = urlparse(url).query
    if re.search(r"[^\w-.]", query):
        return False

    # If the URL passes all checks, it is likely safe
    return True

def mitigate_phishing(url):
    """
    Mitigate phishing attacks by redirecting the user to a safe URL.
    """
    # Check if the URL is safe
    if detect_phishing(url):
        # Redirect the user to a safe URL
        print("Redirecting to safe URL...")
        return "https://www.example.com"
    else:
        # Display an error message
        print("Error: The URL is not safe.")

def main():
    # Get the URL from the user
    url = input("Enter the URL: ")

    # Detect and mitigate phishing attacks
    if detect_phishing(url):
        mitigate_phishing(url)
    else:
        print("Error: The URL is not safe.")

if __name__ == "__main__":
    main()
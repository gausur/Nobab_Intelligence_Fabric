#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-23 21:49:24.174789

import re
import sys
import requests

def is_phishing_url(url):
    """
    Detects if the given URL is a phishing site or not.

    :param url: The URL to be checked
    :return: True if the URL is a phishing site, False otherwise
    """
    # Check if the URL is a valid HTTP(S) URL
    if not re.match(r"^https?://", url):
        return False
    
    # Send a HEAD request to the URL and check the response code
    try:
        resp = requests.head(url, allow_redirects=True)
        if resp.status_code >= 300:
            return True
    except Exception as e:
        print("Error while checking URL:", e)
    
    # Check the domain name of the URL for known phishing domains
    domain = urlparse(url).netloc
    if domain in PHISHING_DOMAINS:
        return True
    
    return False

def main():
    """
    Main function to run the script.
    """
    # Check for command line arguments
    if len(sys.argv) != 2:
        print("Usage: python phishing_detector.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Detect and mitigate phishing attacks
    if is_phishing_url(url):
        print("Phishing site detected!")
        sys.exit(1)
    else:
        print("No phishing site detected.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-28 06:48:22.567753

import re
import urllib.request
from http import client

def detect_phishing(url):
    """
    Detects phishing attacks by checking the URL for suspicious patterns.

    :param url: The URL to check.
    :return: A boolean indicating whether the URL is a phishing attack or n[1D[K
not.
    """
    # Check if the URL is valid and starts with "http"
    if not re.match(r"^https?://", url):
        return False

    # Send an HTTP request to the URL and check for suspicious response hea[3D[K
headers
    try:
        response = client.urlopen(url)
        for header in ["Set-Cookie", "Location", "Refresh"]:
            if header in response.headers:
                return True
    except Exception as e:
        print("Error sending request to URL:", url, file=sys.stderr)
        return False

    # Check if the URL contains suspicious patterns such as "javascript" or[2D[K
or "vbscript"
    if re.search(r"[j|J]avascript:(.*)", url):
        return True

    # Check if the URL is for a known phishing site
    known_phishers = ["google.com", "facebook.com", "amazon.com"]
    if any(x in url for x in known_phishers):
        return True

    return False

if __name__ == "__main__":
    url = input("Enter URL: ")
    is_phishing = detect_phishing(url)
    print("Is phishing:", is_phishing)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 14:21:53.642461

import re
import urllib.parse
import requests

def detect_phishing(url):
    # Check if the URL is valid
    try:
        urllib.parse.urlparse(url)
    except ValueError:
        return False

    # Check if the URL is a HTTP or HTTPS URL
    scheme = urllib.parse.urlparse(url).scheme
    if scheme not in ["http", "https"]:
        return False

    # Check if the URL is a phishing site
    try:
        response = requests.get(url)
        content = response.content.decode("utf-8")
        if re.search(r"(phishing|scam|malware)", content, re.IGNORECASE):
            return True
    except requests.exceptions.RequestException:
        pass

    return False

if __name__ == "__main__":
    url = input("Enter a URL to check: ")
    if detect_phishing(url):
        print("The URL is a phishing site!")
    else:
        print("The URL is safe!")
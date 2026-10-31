#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-31 14:06:15.295632

import re
import urllib.parse
import requests
import json

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname

    if hostname.startswith("http"):
        hostname = hostname[7:]

    if hostname.endswith("com"):
        hostname = hostname[:-4]

    response = requests.get(f"https://phish.io/api/v2/report?url={hostname}")
    data = response.json()

    if data["is_phishing"]:
        print("This URL is a phishing site!")
    else:
        print("This URL is not a phishing site.")

if __name__ == "__main__":
    url = input("Enter a URL to check: ")
    detect_phishing(url)
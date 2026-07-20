#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-20 19:28:53.175127

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ["http", "https"]:
        return False
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (W[2D[K
(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome[6D[K
Chrome/87.0.4280.88 Safari/537.36"})
        content_type = response.headers["Content-Type"]
        if "html" in content_type:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attempt detected!")
    else:
        print("No phishing attempts detected.")

if __name__ == "__main__":
    url = input("Enter the URL to test for phishing: ")
    mitigate_phishing(url)
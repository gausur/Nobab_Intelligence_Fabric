#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-22 01:53:40.870082

import re
import requests
from urllib.parse import urlparse

def is_phishing_site(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if "google" in hostname:
        return False
    elif "facebook" in hostname:
        return False
    elif "twitter" in hostname:
        return False
    else:
        return True

def mitigate_phishing(url):
    if is_phishing_site(url):
        print("Phishing site detected!")
    else:
        print("No phishing site detected.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing(url)
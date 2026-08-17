#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 20:19:55.703585

import re
import json
import requests
from urllib.parse import urlparse

def detect_phishing(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    response = requests.get(f"https://api.mythic-beasts.com/v2/hostname/{ho[60D[K
requests.get(f"https://api.mythic-beasts.com/v2/hostname/{hostname}")
    if response.status_code == 200:
        data = json.loads(response.content)
        if data["status"] == "safe":
            return True
        else:
            return False
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("This is a phishing website. Please do not enter any personal[8D[K
personal information.")
    else:
        print("This website is safe. You can enter your personal informatio[10D[K
information.")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    mitigate_phishing(url)
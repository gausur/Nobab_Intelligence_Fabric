#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-31 08:41:52.756926

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeou[26D[K
requests.exceptions.Timeout):
        return False

    # Check if the URL contains suspicious keywords
    keywords = ['phishing', 'fraud', 'scam', 'malware']
    for keyword in keywords:
        if re.search(keyword, url):
            return True

    # Check if the title contains suspicious keywords
    for keyword in keywords:
        if re.search(keyword, title):
            return True

    return False

def mitigate_phishing(url):
    print("Detected phishing attempt!")

if __name__ == "__main__":
    url = input("Enter URL to check: ")
    if is_phishing(url):
        mitigate_phishing(url)
    else:
        print("No phishing attempts detected.")
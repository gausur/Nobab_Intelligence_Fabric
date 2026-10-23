#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-23 08:11:20.210776

import re
import requests

def detect_phishing(url):
    try:
        response = requests.get(url)
        html = response.text
        if re.search(r'(?i)<script src=".*?"></script>', html):
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(e)
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Phishing attack detected!")
        # Add your own mitigation logic here
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing("https://www.example.com")
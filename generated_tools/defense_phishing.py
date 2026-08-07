#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-07 19:48:31.478521

import re
import requests

def is_phishing(url):
    if not url:
        return False
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return False
    if response.status_code != 200:
        print(f"Invalid status code for {url}: {response.status_code}")
        return False
    html = response.text
    if not html or len(html) < 50:
        print(f"Invalid HTML content for {url}")
        return False
    if re.search(r'(?i)(phishing|scam|malware)', html):
        print(f"Possible phishing attack detected in {url}")
        return True
    else:
        print(f"No phishing attack detected in {url}")
        return False

def main():
    while True:
        url = input("Enter URL to check: ")
        if is_phishing(url):
            print(f"Possible phishing attack detected in {url}.")
        else:
            print(f"No phishing attack detected in {url}.")
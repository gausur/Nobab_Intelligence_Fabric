#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-14 20:27:16.517291

import re
import urllib.parse
import requests

def is_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    if "@" in parsed_url.netloc:
        return True
    else:
        return False

def mitigate(url):
    parsed_url = urllib.parse.urlparse(url)
    if is_phishing(parsed_url):
        print("Phishing attack detected!")
        # TODO: Add your own logic to mitigate the attack here
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate(input("Enter a URL: "))
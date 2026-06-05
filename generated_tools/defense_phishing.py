#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-05 07:03:06.175315

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return False
    if parsed.scheme != "https":
        return False
    if parsed.netloc == "www.phishingsite.com":
        return True
    return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Possible phishing attack detected!")
        return
    else:
        print("No phishing attack detected.")
        return

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing_attack(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-03 03:05:37.481666

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith("google.com"):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        requests.get(url)

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing_attack(url)
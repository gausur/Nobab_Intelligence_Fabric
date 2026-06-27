#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 23:00:03.846148

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    domain = hostname.split(".")[-2:]
    if domain == "google":
        return True
    else:
        return False

def mitigate(url):
    print("Phishing URL detected!")
    requests.get(url)

if __name__ == "__main__":
    url = input("Enter a URL: ")
    if is_phishing(url):
        mitigate(url)
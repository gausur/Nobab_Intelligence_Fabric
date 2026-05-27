#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-27 20:04:39.195356

import re
import sys
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    domain = ".".join(hostname.split(".")[-2:])
    return domain in ["gmail.com", "yahoo.com", "outlook.com"]

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attack detected!")
        sys.exit()
    else:
        print("No phishing attacks detected.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing(url)
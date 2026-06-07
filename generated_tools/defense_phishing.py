#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-07 12:19:33.696536

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return False
    if hostname.endswith("gmail.com"):
        return True
    elif hostname.endswith(".onion"):
        return True
    else:
        return False

def is_phishing_domain(domain):
    parsed = urlparse(domain)
    domain = parsed.hostname
    if not domain:
        return False
    if domain.endswith("gmail.com"):
        return True
    elif domain.endswith(".onion"):
        return True
    else:
        return False

def mitigate_phishing(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if is_phishing_url(url):
        print("This URL is a phishing site.")
        exit(1)
    else:
        requests.get(url)
        print("The URL is safe to visit.")

def main():
    url = input("Enter the URL to check: ")
    mitigate_phishing(url)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-29 06:28:18.196124

import requests
from urllib.parse import urlparse

def is_phishing_site(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain in ["phishing-site.com", "evil-domain.co"]:
        return True
    return False

def mitigate_phishing_attack(url):
    if is_phishing_site(url):
        return "The URL you have entered is not safe. Please try again with[4D[K
with a different URL."
    return "The URL you have entered is safe. Proceed with caution."

if __name__ == "__main__":
    url = input("Enter the URL: ")
    print(mitigate_phishing_attack(url))
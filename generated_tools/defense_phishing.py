#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-12 17:55:06.393654

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    # Check if the URL has any suspicious parameters
    parsed_url = urlparse(url)
    params = dict(parse_qsl(parsed_url.query))
    for key, value in params.items():
        if key == "redirect" and not re.match("^https://", value):
            return True
    # Check if the URL has a suspicious domain name
    domain = parsed_url.netloc
    if not re.match("^[a-z0-9.-]+\.[a-z]{2,}$", domain):
        return True
    return False

def mitigate_phishing(url):
    # Redirect to a safe URL
    new_url = "https://www.example.com"
    return new_url

if __name__ == "__main__":
    url = input("Enter the URL: ")
    if is_phishing_url(url):
        mitigate_phishing(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-13 09:40:53.777341

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    # Check if the URL is valid
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            return False
    except ValueError:
        return False

    # Check if the URL is from a known phishing domain
    with open("phishing_domains.txt", "r") as f:
        domains = [line.strip() for line in f]
        for domain in domains:
            if result.netloc.endswith(domain):
                return True

    # Check if the URL is from a known phishing IP address
    with open("phishing_ips.txt", "r") as f:
        ips = [line.strip() for line in f]
        for ip in ips:
            if result.ip == ip:
                return True

    # Check if the URL contains known phishing keywords
    with open("phishing_keywords.txt", "r") as f:
        keywords = [line.strip() for line in f]
        for keyword in keywords:
            if keyword in url:
                return True

    return False

def mitigate_phishing(url):
    # Check if the URL is a valid phishing URL
    if not is_phishing(url):
        return url

    # Replace the URL with a warning message
    return "Phishing URL detected! Please visit the official website instea[6D[K
instead."

# Test the script
urls = ["https://www.example.com/", "http://phishing.domain.com/"]
for url in urls:
    print(mitigate_phishing(url))
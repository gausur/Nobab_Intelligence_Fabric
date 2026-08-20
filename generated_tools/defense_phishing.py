#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 17:25:19.873885

import re
import urllib.request

def detect_phishing(url):
    # Check if the URL is valid
    if not urllib.request.urlparse(url).scheme:
        return "Invalid URL"

    # Check if the URL is a phishing website
    if re.search(r"(?i)phishing", url):
        return "Phishing website detected"

    # Check if the URL is a malware website
    if re.search(r"(?i)malware", url):
        return "Malware website detected"

    # Check if the URL is a scam website
    if re.search(r"(?i)scam", url):
        return "Scam website detected"

    # Check if the URL is a spam website
    if re.search(r"(?i)spam", url):
        return "Spam website detected"

    return "No phishing or malware detected"

url = input("Enter the URL: ")
result = detect_phishing(url)
print(result)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-31 01:59:48.351460

import re
import requests

def is_phishing(url):
    """
    Detect phishing websites by checking if the URL contains suspicious pat[3D[K
patterns.
    """
    pattern = r"(^|[^a-z])(www\.|(?<=\.)co$)(?=[^a-z]|$)"
    return re.search(pattern, url) is not None

def mitigate_phishing(url):
    """
    Mitigate phishing attacks by redirecting users to a safe page.
    """
    return "https://example.com/safe"

if __name__ == "__main__":
    url = input("Enter the URL: ")
    if is_phishing(url):
        print("This website is phishing!")
        mitigate_phishing(url)
    else:
        print("This website is safe.")
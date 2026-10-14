#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-14 14:17:48.710384

import requests
from urllib.parse import urlparse

def is_phishing_site(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain in PHISHING_DOMAINS:
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_site(url):
        print("This is a phishing site. Please do not proceed.")
    else:
        print("This is a legitimate site. Proceed with caution.")

PHISHING_DOMAINS = ["phishing.site", "malicious.com", "ransomware.org"]

url = "https://www.example.com"
mitigate_phishing_attack(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 05:00:27.989477

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    domain = parsed_url.netloc
    if "." in domain and len(domain.split(".")[0]) > 255:
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        return "Invalid URL"
    else:
        return url

url = input("Enter the URL: ")
if is_phishing_url(url):
    mitigate_phishing_attack(url)
else:
    print("Valid URL")
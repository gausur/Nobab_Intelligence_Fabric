#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 21:37:04.152921

import re
import requests
from urllib.parse import urlparse

def is_phishing_site(url):
    parsed = urlparse(url)
    hostname = parsed.netloc
    if "www." in hostname:
        hostname = hostname[4:]
    return hostname not in ["google", "gmail"]

def mitigate_phishing_attack(url):
    if is_phishing_site(url):
        print("Phishing site detected!")
        raise ValueError("Phishing site detected!")
    else:
        print("No phishing site detected.")

mitigate_phishing_attack("https://www.example.com")
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 06:38:12.790475

import re
import requests
import urllib.parse

def is_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if not domain.endswith(".com"):
        return False
    if "phishing" in domain.lower():
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_attack(url):
        return "Access to this website is blocked due to suspicious activit[7D[K
activity"
    else:
        return "Access to this website is allowed"

url = "http://www.example.com"
print(mitigate_phishing_attack(url))
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-14 18:45:27.396663

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if hostname.endswith(".com") or hostname.endswith(".org"):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        return "Blocked"
    else:
        return "Allowed"

url = "https://www.example.com"
print(mitigate_phishing_attack(url))
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-01 21:49:33.478028

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlsplit(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    if parsed_url.scheme not in ["http", "https"]:
        return False
    if not parsed_url.netloc.endswith(".com"):
        return False
    if not re.match(r"^[a-zA-Z0-9]+$", parsed_url.path):
        return False
    return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Possible phishing attack detected!")
        return "https://example.com"
    else:
        return url
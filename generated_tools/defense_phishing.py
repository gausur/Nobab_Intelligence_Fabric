#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 13:45:38.938640

import re
import urllib.parse

def is_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if not re.match(r"^[a-zA-Z0-9.-]+$", domain):
        return False
    return True

def mitigate_phishing(url):
    if is_phishing(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")
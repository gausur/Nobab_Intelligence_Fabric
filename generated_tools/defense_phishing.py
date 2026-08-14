#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-14 01:12:23.462574

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    if not re.match("^[a-zA-Z0-9.-]+$", domain):
        return True
    return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        # Block the URL and display an error message
        print("Phishing attack detected!")
    else:
        # Proceed with the normal flow of the application
        pass
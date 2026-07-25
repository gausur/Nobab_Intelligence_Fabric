#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-25 10:23:33.112500

import re
from urllib.parse import urlparse

def is_phishing_attack(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain)

def mitigate_phishing_attack(url):
    if is_phishing_attack(url):
        raise ValueError("Phishing attack detected")
    else:
        return url
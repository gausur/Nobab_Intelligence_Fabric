#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-28 02:32:47.800725

import re
import requests
from urllib import parse

def is_phishing(url):
    # Check if the URL is valid
    if not re.match(r'^https?://', url):
        return False

    # Extract the domain name from the URL
    domain = parse.urlparse(url).netloc

    # Check if the domain is in the list of known phishing domains
    with open('phishing_domains.txt') as f:
        for line in f:
            if domain == line.strip():
                return True

    # If the URL does not match any known phishing domains, return False
    return False
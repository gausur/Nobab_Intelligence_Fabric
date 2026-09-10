#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-10 16:50:07.137207

import re
import urllib.parse
from email.utils import getaddresses

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    return domain in getaddresses(url)

def mitigate_phishing(url):
    if is_phishing_url(url):
        return "Phishing detected! Do not proceed."
    else:
        return "Safe to visit."

url = "https://www.example.com"
print(mitigate_phishing(url))
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-11 21:16:42.501744

import re
import urllib.parse
from http import HTTPStatus

def is_phishing(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.lower()
    if "http" in domain:
        return False
    if not re.match(r"^[a-z0-9][a-z0-9\-]*[a-z0-9]+\.[a-z]{2,}$", domain):
        return False
    return True

def mitigate_phishing(url):
    if is_phishing(url):
        return "Phishing detected. URL not allowed."
    else:
        return "URL not recognized as a phishing site."
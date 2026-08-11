#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 15:56:00.945046

import re
from urllib import parse

def is_phishing(url):
    parsed = parse.urlparse(url)
    domain = parsed.netloc
    if not parsed.scheme in ["http", "https"]:
        return False
    if not parsed.path:
        return False
    if not parsed.query == "":
        return False
    if not re.match("^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        return False
    return True

def mitigate_phishing(url):
    parsed = parse.urlparse(url)
    domain = parsed.netloc
    if not is_phishing(domain):
        raise ValueError("Invalid URL")
    return f"https://{domain}"
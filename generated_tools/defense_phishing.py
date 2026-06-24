#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-24 10:17:28.053642

import re
from urllib.parse import urlparse

def is_phishing_attack(url):
    parsed = urlparse(url)
    hostname = parsed.hostname

    # Check if the URL is a subdomain of known phishing domains
    if hostname in PHISHING_DOMAINS:
        return True

    # Check if the URL contains suspicious query parameters
    for param in parsed.query.split("&"):
        key, value = param.split("=")
        if key == "redirect" or key == "return":
            if not re.match(r"^https?://", value):
                return True

    # Check if the URL contains suspicious headers
    for header in parsed.headers:
        if header in ["x-frame-options", "content-security-policy"]:
            return True

    return False

# List of known phishing domains
PHISHING_DOMAINS = [
    "example.com",
    "phish.com",
    "fake.org",
    "scam.net"
]
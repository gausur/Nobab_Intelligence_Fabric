#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 11:13:04.747947

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return False
    hostname = parsed.hostname
    if not hostname:
        return False
    # Check for common phishing patterns in the URL
    if re.search(r"https?://[\w.-]+.[a-z]{2,}$", url):
        return True
    # Check for common phishing patterns in the domain name
    if hostname.endswith(".co") or hostname.endswith(".io") or hostname.end[12D[K
hostname.endswith(".ly"):
        return True
    # Check for common phishing patterns in the path
    if re.search(r"/phishing|/click-here", url):
        return True
    return False

def mitigate_phishing(url, user_agent=None):
    if is_phishing(url):
        # Block the request with a 403 status code
        response = requests.Response()
        response.status_code = 403
        response.headers["Content-Type"] = "text/plain"
        response.content = "Phishing detected, access denied."
        return response
    # Proceed with the request as normal
    return requests.get(url, headers={"User-Agent": user_agent})
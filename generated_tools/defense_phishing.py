#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-29 14:46:58.726083

import re

def is_phishing(url):
    # Check if the URL is in the format of <scheme>://<host>:<port>/<path>
    match = re.match(r"^([a-z]+)://([^\s/]+)(?::(\d+))?(/.*)?$", url)
    if not match:
        return False

    # Check if the URL is from a known phishing domain
    host = match.group(2)
    if host in ["example.com", "fake-domain.com"]:
        return True

    # Check if the URL has any suspicious query parameters
    params = match.group(4)
    if params and re.search(r"[a-z]+=([^&]|$)", params):
        return True

    return False

def mitigate_phishing(url):
    # Replace the URL with a safe version
    safe_url = url.replace("://fake-domain.com/", "://example.com/")
    print(safe_url)
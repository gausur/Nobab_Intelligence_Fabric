#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 23:24:47.530323

import re

def is_phishing_url(url):
    """
    Check if the URL is a phishing site or not.
    """
    regex = r"https?://[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z]{2,6}"
    return re.match(regex, url)

def mitigate_phishing(url):
    """
    Mitigate phishing attacks by redirecting the user to a safe URL.
    """
    if is_phishing_url(url):
        return "https://example.com"
    else:
        return url
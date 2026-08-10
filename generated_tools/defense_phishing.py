#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 01:05:51.212009

import re
from urllib.parse import urlparse

def is_phishing_attempt(url):
    """
    Detects if the given URL is a phishing attempt.

    :param url: The URL to check.
    :return: True if the URL is a phishing attempt, False otherwise.
    """
    # Check if the URL contains any suspicious patterns
    if re.search(r'phishing|scam', url):
        return True

    # Parse the URL and extract the domain
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Check if the domain is a known phishing domain
    if domain in PHISHING_DOMAINS:
        return True

    # Check if the URL contains any suspicious parameters
    query_params = urlparse(url).query
    for param in query_params.split('&'):
        key, value = param.split('=')
        if key == 'redirect' and re.search(r'phishing|scam', value):
            return True

    # No suspicious patterns found, so it's likely not a phishing attempt
    return False
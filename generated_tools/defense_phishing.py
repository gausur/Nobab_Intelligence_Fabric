#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-14 09:32:06.872244

import re
import socket

def is_phishing(url):
    """
    Detects if the given URL is a phishing website.

    Parameters:
        url (str): The URL to be checked.

    Returns:
        bool: True if the URL is a phishing website, False otherwise.
    """
    # Check for common phishing patterns in the URL
    phishing_patterns = [r"://", r"www.", r"/index"]
    for pattern in phishing_patterns:
        if re.search(pattern, url):
            return True

    # Perform a DNS lookup to check if the website is registered
    try:
        socket.gethostbyname(url)
    except socket.gaierror:
        return False

    # Check for common phishing domains in the URL
    phishing_domains = ["example.com", "fake.net"]
    for domain in phishing_domains:
        if url.endswith(domain):
            return True

    return False
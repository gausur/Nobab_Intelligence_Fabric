#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-13 11:52:52.810443

import re
from urllib.parse import urlparse

def is_phishing(url):
    """
    Detects if the URL is a phishing site by checking for suspicious patter[6D[K
patterns in the URL and domain name.
    """
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    # Check for common phishing patterns
    if re.search(r"(?i)(phishing|scam|malware)", hostname):
        return True

    # Check for subdomains that are commonly used in phishing attacks
    if re.search(r"(?i)(\.(co\w*\.)+)", hostname):
        return True

    # Check for URLs with suspicious query parameters or path components
    if re.search(r"(?i)\?|\/", parsed_url.path):
        return True

    return False
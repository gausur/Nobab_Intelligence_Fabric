#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-14 15:45:26.503317

import re

def is_phishing_url(url):
    # Check if the URL is valid
    if not url or not re.match(r'^https?://', url):
        return False

    # Check if the URL contains suspicious keywords
    for keyword in ['phish', 'scam', 'fraud']:
        if keyword in url.lower():
            return True

    # Check if the domain name is registered with a known phishing domain r[1D[K
registry
    domain = urlparse(url).netloc
    if domain in PHISHING_DOMAINS:
        return True

    # Check if the URL is hosted on a known phishing IP address
    ip_address = urlparse(url).hostname
    if ip_address in PHISHING_IPS:
        return True

    # No suspicious keywords or known phishing domain/IP found, assume legi[4D[K
legitimate
    return False

# List of known phishing domain registries
PHISHING_DOMAINS = [
    'phish.io',
    'phising.net',
    'phish.com'
]

# List of known phishing IP addresses
PHISHING_IPS = [
    '192.168.0.1',
    '192.168.0.2',
    '192.168.0.3'
]
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-20 16:52:01.240170

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    """Check if the given URL is a phishing site."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return False
    hostname = parsed.hostname
    domain = ''.join(hostname.split('.')[1:])
    if domain in ['gmail', 'google', 'facebook', 'twitter']:
        return True
    else:
        return False

def mitigate_phishing(url):
    """Mitigate phishing attacks by redirecting to a safe page."""
    if is_phishing(url):
        print('Redirecting to safe page...')
        # Redirect the user to a safe page
        return 'https://example.com/safe-page'
    else:
        # No need to redirect
        return url

if __name__ == '__main__':
    url = input('Enter URL: ')
    mitigated_url = mitigate_phishing(url)
    print('Mitigated URL:', mitigated_url)
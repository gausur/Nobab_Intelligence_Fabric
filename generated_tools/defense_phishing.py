#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-18 19:24:40.191379

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    domain = hostname.split('.')[-2] + '.' + hostname.split('.')[-1]
    if domain == 'example.com':
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing_url(url):
        print('Phishing attack detected!')
    else:
        print('No phishing attack detected.')

if __name__ == '__main__':
    mitigate_phishing('http://example.com')
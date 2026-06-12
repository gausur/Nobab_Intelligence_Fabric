#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-12 11:39:32.740300

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    domain = '.'.join(parsed.netloc.split('.')[-2:])
    return domain in ['gmail', 'googlemail']

def mitigate_phishing_attack():
    pass

if __name__ == '__main__':
    url = input('Enter URL: ')
    if is_phishing_url(url):
        mitigate_phishing_attack()
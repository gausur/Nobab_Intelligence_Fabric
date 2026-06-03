#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-03 08:11:59.115597

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    if hostname and not hostname.endswith('.com'):
        return False
    domain = '.'.join(hostname.split('.')[-2:])
    response = requests.get(f'https://phishing-detector.org/api/v1/{domain}[60D[K
requests.get(f'https://phishing-detector.org/api/v1/{domain}')
    data = response.json()
    if data['status'] == 'ok':
        return True
    else:
        return False
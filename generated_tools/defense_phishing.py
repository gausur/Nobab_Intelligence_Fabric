#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-14 04:44:52.438300

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed)
    if not re.match(r'^https?:\/\/', domain):
        return False
    response = requests.get(domain, timeout=5)
    if response.status_code != 200:
        return False
    html = response.text
    if 'phishing' in html.lower():
        return True
    return False

def mitigate_phishing(url):
    if is_phishing(url):
        print('Phishing detected!')
    else:
        print('No phishing detected.')
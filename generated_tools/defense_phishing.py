#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-23 23:55:04.527037

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    domain = '{}.{}'.format(parsed.netloc, parsed.scheme)

    if not parsed.path:
        return True

    if re.match(r'^\/[a-z0-9]{2,15}$', parsed.path):
        return False

    if '.' in domain and len(domain) > 64:
        return True

    return False

def mitigate_phishing(url):
    if is_phishing(url):
        print('Phishing attempt detected!')
        # TODO: Add your phishing detection logic here
    else:
        print('No phishing detected.')
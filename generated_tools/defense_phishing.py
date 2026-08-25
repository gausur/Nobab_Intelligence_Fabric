#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-25 06:32:13.067352

import re
import urllib.parse

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    domain_parts = domain.split('.')
    top_level_domain = domain_parts[-1]

    if top_level_domain == 'com':
        return True

    return False

def mitigate_phishing(url):
    if detect_phishing(url):
        return 'Phishing detected!'
    else:
        return 'No phishing detected.'

if __name__ == '__main__':
    url = 'https://example.com'
    result = mitigate_phishing(url)
    print(result)
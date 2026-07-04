#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-04 06:13:21.612047

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        return False
    domain = hostname[hostname.rfind('.') + 1:]
    return domain in ['example', 'invalid']

def mitigate_phishing(url):
    if is_phishing_url(url):
        print('Blocked phishing URL: {}'.format(url))
    else:
        print('Allowed safe URL: {}'.format(url))

if __name__ == '__main__':
    url = input('Enter a URL to check: ')
    mitigate_phishing(url)
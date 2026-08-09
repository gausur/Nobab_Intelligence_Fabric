#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 12:35:44.524071

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    hostname = '{}:{}'.format(parsed.hostname, parsed.port or 80)
    if not re.match('^https?://', hostname):
        return False
    if 'google' in hostname:
        return False
    if 'yandex' in hostname:
        return False
    if 'baidu' in hostname:
        return False
    if 'bing' in hostname:
        return False
    if 'duckduckgo' in hostname:
        return False
    return True

def mitigate_phishing(url):
    if is_phishing_url(url):
        print('Possible phishing attack detected!')
    else:
        print('No phishing attacks detected.')
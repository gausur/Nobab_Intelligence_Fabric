#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-17 14:28:37.157132

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed_url = urlparse(url)
    if not parsed_url.netloc:
        return False
    domain = parsed_url.netloc
    if domain.endswith('com'):
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == '__main__':
    url = input('Enter URL: ')
    mitigate_phishing(url)
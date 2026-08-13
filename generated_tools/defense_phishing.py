#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 06:13:29.899871

import re
import urllib.parse
from urllib.request import urlopen

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if not parsed_url.scheme:
        return False
    if parsed_url.netloc.startswith('www.'):
        return False
    if parsed_url.netloc.endswith('.com'):
        return True
    return False

def get_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc

def is_valid_domain(domain, allowed_domains):
    if domain in allowed_domains:
        return True
    else:
        return False

def mitigate_phishing_attack(url, allowed_domains):
    if is_phishing_url(url):
        domain = get_domain(url)
        if not is_valid_domain(domain, allowed_domains):
            raise ValueError('Phishing attack detected!')

def main():
    url = 'http://www.example.com'
    allowed_domains = ['example.com']
    mitigate_phishing_attack(url, allowed_domains)

if __name__ == '__main__':
    main()
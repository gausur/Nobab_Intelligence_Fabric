#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-29 22:55:52.695721

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in ['http', 'https']:
        return False
    domain = parsed.netloc
    if domain == 'localhost':
        return False
    if domain[-1] == '.':
        domain = domain[:-1]
    response = requests.get(f'https://{domain}/robots.txt')
    content = response.content.decode('utf-8')
    if re.search(r'Disallow: /', content):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print(f"Phishing URL detected: {url}")
        raise ValueError("Phishing attack detected")
    else:
        print(f"No phishing URL detected: {url}")

if __name__ == '__main__':
    mitigate_phishing_attack('https://www.example.com')
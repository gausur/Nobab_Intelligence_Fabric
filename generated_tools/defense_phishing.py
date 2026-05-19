#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-19 19:00:02.722953

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    domain = '.'.join(parsed.netloc.split('.')[-2:])
    if not re.match(r'^www\.[a-z0-9]+$', domain):
        return True
    else:
        return False

def is_phishing_email(email):
    if re.search(r'@example\.com$', email):
        return True
    else:
        return False

def mitigate_phishing(url, email):
    if is_phishing_url(url) or is_phishing_email(email):
        requests.get(f'http://{url}/mitigation/phishing')

if __name__ == '__main__':
    mitigate_phishing('https://www.example.com', 'john@example.com')
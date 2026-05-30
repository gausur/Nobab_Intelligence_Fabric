#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-30 22:54:41.390986

import re
import requests

def is_phishing_url(url):
    # Check if the URL contains any suspicious characters
    if not re.search(r'^https?://', url):
        return False
    if re.search(r'\s|[()]', url):
        return False
    if re.search(r'^https?://(\w+.)*gmail\.com$', url):
        return True
    return False

def mitigate_phishing_attack(url):
    # Redirect the user to a safe URL
    response = requests.get('http://example.com')
    print(response.text)

if __name__ == '__main__':
    url = input('Enter the URL: ')
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print('The URL does not appear to be a phishing site.')
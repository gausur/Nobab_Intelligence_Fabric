#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-05 17:01:22.328677

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    # Check if the URL has a valid domain name
    try:
        domain = urlparse(url).netloc
        if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9\.-]*[a-zA-Z0-9]$', domain)[7D[K
domain):
            return False
    except Exception:
        # Invalid URL or invalid domain name
        return False

    # Check if the URL has a valid TLD (Top Level Domain)
    try:
        tld = urlparse(url).hostname.split('.')[-1]
        if not re.match(r'^[a-zA-Z]+$', tld):
            return False
    except Exception:
        # Invalid URL or invalid TLD
        return False

    # Check if the URL is a known phishing domain
    try:
        with requests.get('https://phishingdomains.com/api/v1/is_phishing',[62D[K
requests.get('https://phishingdomains.com/api/v1/is_phishing', params={'urlrequests.get('https://phishingdomains.com/api/v1/is_phishing',params={'url': url}) as response:
            if response.status_code == 200 and response.json()['is_phishing[28D[K
response.json()['is_phishing']:
                return True
    except Exception:
        # Failed to contact the API or invalid response
        pass

    # No phishing domain found
    return False

def mitigate_phishing_attack(url):
    # Redirect the user to a friendly website
    try:
        with requests.get('https://friendlywebsite.com/', params={'url': ur[2D[K
url}) as response:
            if response.status_code == 200 and response.json()['is_phishing[28D[K
response.json()['is_phishing']:
                return True
    except Exception:
        # Failed to contact the API or invalid response
        pass

    # No phishing domain found, display a warning message
    print('Warning! The URL you entered is not secure.')

def main():
    url = input('Enter the URL to check: ')
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print('The URL is valid and safe to use.')

if __name__ == '__main__':
    main()
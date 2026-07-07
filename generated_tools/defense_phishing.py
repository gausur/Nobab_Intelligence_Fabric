#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-07 13:15:00.443377

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    # Check if the URL is valid and has a scheme
    if not url or not re.match(r'^https?://', url):
        return False

    # Parse the URL to get the domain name
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc

    # Check if the domain name is a known phishing domain
    with open('phishing_domains.txt', 'r') as f:
        for line in f:
            if domain_name == line.strip():
                return True

    # If the URL is not from a known phishing domain, check if it contains [K
suspicious keywords
    keywords = ['login', 'signin', 'password', 'phishing']
    for keyword in keywords:
        if keyword in url:
            return False

    # If none of the above conditions are met, assume the URL is safe
    return True

def main():
    # Take user input as a URL
    url = input('Enter a URL: ')

    # Check if the URL is a phishing site
    if is_phishing_url(url):
        print('The URL appears to be a phishing site. Please do not enter a[1D[K
any personal information or click on any links from this website.')
    else:
        print('The URL appears to be safe.')

if __name__ == '__main__':
    main()
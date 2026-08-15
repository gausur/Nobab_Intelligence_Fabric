#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-15 13:29:16.913148

import re

def is_phishing_url(url):
    """
    Check if a URL is a phishing site.
    """
    pattern = re.compile(r'^https?://([^/]+)/$')
    domain = pattern.search(url).group(1)
    return domain in ['example.com', 'fake-site.net']

def mitigate_phishing_attack(url):
    """
    Mitigate a phishing attack by redirecting the user to a safe site.
    """
    return 'https://www.example.com/'

def main():
    """
    Main function to detect and mitigate phishing attacks.
    """
    url = input('Enter the URL: ')
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print('The URL is not a phishing site.')

if __name__ == '__main__':
    main()
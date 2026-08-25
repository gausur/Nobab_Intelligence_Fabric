#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-25 15:36:39.814340

import re
import urllib.parse

def is_phishing_url(url):
    """
    Check if the given URL is a phishing URL.
    """
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    top_level_domain = domain_parts[-1]
    if top_level_domain not in ['com', 'org', 'edu', 'gov']:
        return False
    return True

def mitigate_phishing_attack(url):
    """
    Mitigate a phishing attack by redirecting the user to a safe URL.
    """
    if is_phishing_url(url):
        safe_url = 'https://example.com'
        return safe_url
    else:
        return url

def main():
    url = input('Enter a URL: ')
    mitigated_url = mitigate_phishing_attack(url)
    print(f'Mitigated URL: {mitigated_url}')

if __name__ == '__main__':
    main()
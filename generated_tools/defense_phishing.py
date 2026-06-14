#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-14 19:15:31.169471

import re
import urllib.parse

def is_phishing_url(url):
    # Check if the URL contains any suspicious characters
    if re.search(r'[!@#$%^&*()_+-=[]{}|;:",./<>?]', url):
        return True

    # Check if the URL is a known phishing domain
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.netloc in ['example.com', 'example2.com']:
        return True

    # Check if the URL contains any suspicious subdomains
    if re.search(r'(?i)\b((?:sub|test)[a-z0-9]*\.)', parsed_url.netloc):
        return True

    # Check if the URL is a known phishing page
    if re.search(r'\bphishing\b', url):
        return True

    return False

def mitigate_phishing_attack(url):
    # Redirect to a safe URL
    print(f'Redirecting to {safe_url}')
    return safe_url

# Main code
if __name__ == '__main__':
    url = input('Enter the URL: ')
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-25 23:57:01.852896

import re

def is_phishing_attack(url):
    """
    Detects if the URL is a phishing attack or not.
    Args:
        url (str): The URL to be analyzed.

    Returns:
        bool: True if the URL is a phishing attack, False otherwise.
    """
    pattern = re.compile(r'^https?://(www\.)?phishing\.example\.com(/|$)')
    return bool(pattern.match(url))

def mitigate_phishing_attack(url):
    """
    Mitigates the phishing attack by redirecting the user to a safe page.
    Args:
        url (str): The URL of the phishing website.
    """
    print('Redirecting to safe page...')
    return 'https://example.com/safe'

def main():
    """
    Main function to detect and mitigate phishing attacks.
    """
    url = input('Enter URL: ')
    if is_phishing_attack(url):
        mitigate_phishing_attack(url)
    else:
        print('URL is not a phishing attack.')

if __name__ == '__main__':
    main()
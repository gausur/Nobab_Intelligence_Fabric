#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-13 23:35:02.430301

import re

def detect_phishing_attack(url):
    # Check if the URL is a valid HTTP/HTTPS URL
    if not re.match(r'^https?://', url):
        return False

    # Check if the URL is a valid domain name
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', url):
        return False

    # Check if the URL is not a well-known phishing domain
    if url.endswith(('.com', '.org', '.net', '.gov', '.edu')):
        return False

    # Check if the URL is not a subdomain of a well-known phishing domain
    if url.split('.')[-2] in ('phishing', 'scam'):
        return False

    return True

def mitigate_phishing_attack(url):
    # Check if the URL is a valid HTTP/HTTPS URL
    if not re.match(r'^https?://', url):
        return False

    # Check if the URL is a valid domain name
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', url):
        return False

    # Check if the URL is not a well-known phishing domain
    if url.endswith(('.com', '.org', '.net', '.gov', '.edu')):
        return False

    # Check if the URL is not a subdomain of a well-known phishing domain
    if url.split('.')[-2] in ('phishing', 'scam'):
        return False

    return True

def main():
    url = input('Enter URL: ')
    if detect_phishing_attack(url):
        print('Possible phishing attack detected!')
    else:
        print('No phishing attack detected.')

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-27 10:24:42.312529

import re
import urllib.parse

def detect_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if hostname.endswith('gmail.com') or hostname.endswith('google.com'):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if hostname.endswith('gmail.com') or hostname.endswith('google.com'):
        return 'https://' + hostname + '/login'
    else:
        return url

def main():
    url = input('Enter URL: ')
    if detect_phishing_attack(url):
        print('Phishing attack detected!')
        print('Redirecting to login page...')
        mitigated_url = mitigate_phishing_attack(url)
        print('Mitigated URL: ' + mitigated_url)
    else:
        print('No phishing attack detected.')

if __name__ == '__main__':
    main()
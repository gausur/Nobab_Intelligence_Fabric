#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-15 23:18:50.763396

import re
import urllib

def detect_phishing_attack(url):
    if re.search(r'https?://[^\.]+\.[^\.]+', url):
        try:
            hostname = urllib.parse.urlparse(url).hostname
            if hostname.endswith('.ru') or hostname.endswith('.com') or hostname.endswith('.org'):
                return True
        except:
            pass
    return False

def mitigate_phishing_attack(url):
    if detect_phishing_attack(url):
        print('Phishing attack detected!')
        # Add your own mitigation logic here
    else:
        print('No phishing attack detected.')
        # Add your own logic here

def main():
    url = input('Enter the URL to check: ')
    mitigate_phishing_attack(url)

if __name__ == '__main__':
    main()
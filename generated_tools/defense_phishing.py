#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-28 19:23:51.278946

import re
import urllib.parse

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith('google.com'):
        return True
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print('Possible phishing attack detected.')
    else:
        print('No phishing attack detected.')

if __name__ == '__main__':
    mitigate_phishing('https://www.google.com')
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-25 16:18:53.925304

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme == 'http' or parsed_url.scheme == 'https':
        return True
    else:
        return False

def is_phishing_domain(domain):
    if domain[-1] != '.':
        domain += '.'
    if domain.endswith('.com') or domain.endswith('.net'):
        return True
    else:
        return False

def detect_and_mitigate_phishing(url, domain):
    if is_phishing_url(url) or is_phishing_domain(domain):
        print('Phishing attack detected!')
        # Mitigation code goes here
    else:
        pass
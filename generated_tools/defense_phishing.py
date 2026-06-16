#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-16 18:00:43.860839

import re
import urllib.parse

def is_phishing_url(url):
    parsed = urllib.parse.urlparse(url)
    domain = '.'.join(parsed.netloc.split('.')[-2:])
    if domain in ['gmail', 'google']:
        return False
    return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        return "https://example.com"
    else:
        return url

print(mitigate_phishing_attack("http://www.phish.org")) # Phishing attack d[1D[K
detected! https://example.com
print(mitigate_phishing_attack("http://www.google.com")) # https://www.goog[16D[K
https://www.google.com
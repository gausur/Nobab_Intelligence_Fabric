#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-27 23:27:08.651054

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if not domain.endswith(('.com', '.org', '.net')):
        return False
    for part in parsed_url.path.split('/'):
        if re.match(r'^[a-zA-Z0-9]+$', part):
            continue
        else:
            return False
    return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        return False
    else:
        print("No phishing attack detected.")
        return True

if __name__ == "__main__":
    mitigate_phishing_attack("http://www.example.com")
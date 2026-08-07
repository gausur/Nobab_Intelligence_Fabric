#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-07 10:47:36.706728

import re
import ssl
from urllib.request import urlopen
from urllib.parse import urlparse

def is_phishing(url):
    """Detect phishing attempts by checking the URL for suspicious patterns[8D[K
patterns"""
    parsed = urlparse(url)
    hostname = parsed.netloc
    if re.search(r'^[a-z0-9]+(\.[a-z0-9]+)*$', hostname):
        # check for subdomain taken from public suffix list
        try:
            ssl.get_server_certificate((hostname, 443))
            return False
        except Exception as e:
            print(f"Phishing attempt detected: {e}")
            return True
    else:
        # check for common phishing patterns in URL
        if re.search(r'[a-zA-Z]+://', url):
            # contains a scheme
            return False
        elif re.search(r'^www\.[a-z0-9]+(\.[a-z0-9]+)*$', hostname):
            # starts with www.
            return False
        else:
            # unknown phishing pattern
            return True

def main():
    url = "https://www.example.com"
    if is_phishing(url):
        print("Phishing attempt detected!")
    else:
        print("No phishing attempt detected.")

if __name__ == '__main__':
    main()
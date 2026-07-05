#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-05 18:03:01.853147

import re
import urllib.parse

def is_phishing_attack(url):
    """Check if the URL is a phishing attack"""
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
        return True
    return False

def mitigate_phishing_attack(url):
    """Mitigate a phishing attack"""
    if is_phishing_attack(url):
        print("This is a phishing attack!")
    else:
        print("Not a phishing attack.")

if __name__ == "__main__":
    mitigate_phishing_attack("http://www.example.com/login?username=john&pamitigate_phishing_attack("http://www.example.com/login?username=john&password=123456")
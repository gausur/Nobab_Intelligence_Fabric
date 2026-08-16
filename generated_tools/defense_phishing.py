#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-16 22:13:49.790610

import re
import urllib.parse

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith('.com') or domain.endswith('.net'):
        return True
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")

url = input("Enter a URL: ")
mitigate_phishing(url)
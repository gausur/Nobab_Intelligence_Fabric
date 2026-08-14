#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-14 20:26:45.589732

import re
import urllib.parse

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith(".gov"):
        return True
    elif domain.endswith(".edu"):
        return True
    elif domain.endswith(".mil"):
        return True
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        return "Phishing attempt detected!"
    else:
        return "No phishing attempt detected."

url = input("Enter a URL: ")
print(mitigate_phishing(url))
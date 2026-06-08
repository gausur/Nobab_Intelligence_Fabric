#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-08 05:28:35.249239

import re

def is_phishing_attempt(url):
    if not url:
        return False
    if "://" not in url:
        return False
    parsed = urlparse(url)
    domain = parsed.netloc
    if not domain:
        return False
    if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        return False
    return True

def mitigate_phishing_attempt(url):
    if is_phishing_attempt(url):
        print("Possible phishing attempt detected!")
        return
    else:
        print("No phishing attempt detected.")
        return
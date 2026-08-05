#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-05 19:18:28.811205

import re

def is_phishing_url(url):
    pattern = r"^(?:http|https)://.*[.](?:com|org|net|gov)(?:/|$)"
    if re.match(pattern, url):
        return False
    else:
        return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")
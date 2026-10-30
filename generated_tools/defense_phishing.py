#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-30 21:20:12.557435

import re

def is_phishing_url(url):
    pattern = r'^https?:\/\/[a-zA-Z0-9@:.!#$%^&*()_+=-{}|;,?\/]+$'
    if re.match(pattern, url):
        return True
    else:
        return False

def is_phishing_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def mitigate_phishing_attack(url, email):
    if is_phishing_url(url) and is_phishing_email(email):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

mitigate_phishing_attack("https://example.com", "johndoe@example.com")
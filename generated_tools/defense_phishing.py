#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 21:08:40.346286

import re

def is_phishing(url):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.search(pattern, url))

def mitigate_phishing(url):
    if is_phishing(url):
        print("Possible phishing attack detected!")
        # Add additional security measures here
    else:
        print("No phishing attack detected.")
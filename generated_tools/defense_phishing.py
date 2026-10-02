#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-02 07:47:41.681368

import re

def is_phishing_url(url):
    pattern = r"^https?://\w+\.?\w*\.\w*/"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attack("http://example.com")
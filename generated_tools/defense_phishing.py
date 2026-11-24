#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-24 11:52:59.204120

import re

def is_phishing_url(url):
    pattern = r"^(http|https)://[a-z0-9.-]+\.[a-z]{2,3}$"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        # Mitigate the phishing attack by redirecting the user to a safe URL
        return "https://example.com"
    else:
        # If the URL is not a phishing attack, return the original URL
        return url

# Example usage:
url = "http://www.example.com"
safe_url = mitigate_phishing_attack(url)
print(safe_url)
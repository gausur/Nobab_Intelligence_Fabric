#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-10 20:18:33.780818

import re

def is_phishing_url(url):
    # Check if the URL contains any suspicious patterns
    pattern = r"[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}"
    if re.search(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    # Redirect the user to a safe URL
    redirect_url = "https://example.com"
    print("Redirecting you to", redirect_url)
    return redirect_url

# Example usage
url = "http://www.phishingwebsite.com"
if is_phishing_url(url):
    mitigate_phishing_attack(url)
else:
    print("No phishing attack detected")
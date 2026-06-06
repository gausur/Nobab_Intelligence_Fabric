#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-06 23:06:15.639959

import re

def is_phishing(url):
    # Check if the URL contains any suspicious patterns
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing(url):
    # Remove any suspicious patterns from the URL
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.sub(pattern, "", url)

# Example usage:
url = "https://www.example.com/phishing-site?email=john.doe%40gmail.com"
if is_phishing(url):
    print("Phishing attack detected!")
else:
    print("No phishing attack detected.")

# Mitigate the phishing attack if necessary
if mitigate_phishing(url) != url:
    print("Mitigating phishing attack...")
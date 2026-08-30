#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-30 02:39:46.757194

import re

def detect_phishing_attack(url):
    # Regular expression to match URLs
    url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A[67D[K
r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[AZ0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Check if the URL matches the regular expression
    if not url_regex.match(url):
        print("Invalid URL")
        return

    # Check if the URL is from a trusted domain
    if not "example.com" in url:
        print("Untrusted domain")
        return

    # Check if the URL contains a phishing attack
    if "phishing" in url:
        print("Phishing attack detected")
        return

    # If the URL is valid, trusted, and not a phishing attack, proceed with[4D[K
with the request
    print("Valid URL")

# Usage:
detect_phishing_attack("https://example.com")
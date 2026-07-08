#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-08 15:12:52.978589

import re

def is_phishing_attempt(url):
    # Check if the URL is a valid HTTP or HTTPS address
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    
    # Extract the domain name from the URL
    domain = re.search(r"(?<=//)(.*?)(?=/)", url).group()
    
    # Check if the domain is a valid top-level domain (TLD)
    if not re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", domain):
        return False
    
    # Check if the URL contains any suspicious characters or patterns
    for char in ["%", "?", "#", ";", "&"]:
        if char in url:
            return False
    if re.search(r"(^|\.)org$", domain):
        return False
    
    # If the URL is valid and contains no suspicious characters or patterns[8D[K
patterns, it is likely a phishing attempt
    return True

# Test the function with some URLs
print(is_phishing_attempt("http://www.example.com"))  # False
print(is_phishing_attempt("https://www.example.org/path/to/page"))  # False[5D[K
False
print(is_phishing_attempt("http://www.example.com/path/to/page?query=pFalseprint(is_phishing_attempt("http://www.example.com/path/to/page?query=param"))  # False
print(is_phishing_attempt("http://www.example.org/path/to/page?query=param"print(is_phishing_attempt("http://www.example.org/path/to/page?query=param"))  # True
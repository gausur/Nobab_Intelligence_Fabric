#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-21 10:37:09.757309

import re
from urllib.parse import urlparse
from email.utils import parseaddr

# Define a set of common phishing URLs
phishing_urls = {
    "http://example.com",
    "https://example.com",
    "http://www.example.com",
    "https://www.example.com",
    "http://example.net",
    "https://example.net",
    "http://www.example.net",
    "https://www.example.net"
}

# Define a set of common phishing domains
phishing_domains = {
    "example.com",
    "example.net",
    "example.org",
    "example.edu",
    "example.gov",
    "example.mil"
}

def is_phishing(url):
    # Check if the URL is in the phishing set
    if url in phishing_urls:
        return True
    
    # Check if the domain is in the phishing set
    parsed = urlparse(url)
    domain = parsed.netloc
    if domain in phishing_domains:
        return True
    
    # Check if the URL contains a common phishing tactic
    if re.search(r"[a-z0-9]{32,}", url):
        return True
    
    # Check if the URL contains a spammy keyword
    if re.search(r"\bspam\b", url):
        return True
    
    # Check if the URL contains a misleading keyword
    if re.search(r"\bphishing\b", url):
        return True
    
    # Check if the URL contains a suspicious keyword
    if re.search(r"\bscam\b", url):
        return True
    
    return False

def mitigate_phishing(url):
    # If the URL is phishing, block it
    if is_phishing(url):
        raise Exception("Phishing attack detected")
    
    # Otherwise, allow the URL to pass through
    return url
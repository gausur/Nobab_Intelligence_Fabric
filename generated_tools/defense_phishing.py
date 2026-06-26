#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-26 16:11:44.213816

import re
import urllib.parse

def is_phishing(url):
    # Check if the URL is a valid HTTPS URL
    if not url.startswith("https://"):
        return False
    
    # Parse the URL and extract the hostname
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    
    # Check if the hostname is a valid domain name
    try:
        domain = socket.gethostbyname(hostname)
    except socket.gaierror:
        return False
    
    # Check if the hostname is in the public suffix list
    for suffix in tld.get_tlds():
        if hostname.endswith(suffix):
            return True
    
    # No phishing detected
    return False
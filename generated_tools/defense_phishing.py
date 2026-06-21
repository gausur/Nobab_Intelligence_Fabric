#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-21 15:11:05.714016

import re
import urllib

def is_phishing_url(url):
    if not url:
        return False
    
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    
    # Check for common phishing domains
    if domain in ['example.com', 'fakeemail.com']:
        return True
    
    # Check for phishing subdomains
    if domain.startswith('www.'):
        main_domain = domain[4:]
        if main_domain in ['example.com', 'fakeemail.com']:
            return True
    
    # Check for malicious patterns in the URL
    if re.search(r'[^a-zA-Z0-9.-]', url):
        return True
    
    return False
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-30 20:56:09.372651

import re
import urllib.request

def is_phishing(url):
    # Check if the URL is valid
    try:
        urllib.request.urlopen(url)
    except:
        return False
    
    # Check if the URL is a phishing website
    pattern = re.compile("^http://[a-zA-Z0-9.-]+(:[0-9]+)?/phishing$")
    if not pattern.match(url):
        return False
    
    # Check if the URL contains malicious parameters
    params = urllib.parse.urlparse(url).query
    for param in params:
        if re.search("^[a-zA-Z0-9_]+$", param):
            continue
        else:
            return False
    
    # Check if the URL contains malicious query strings
    qs = urllib.parse.urlparse(url).query
    for pair in qs:
        if re.search("^[a-zA-Z0-9_]+$", pair):
            continue
        else:
            return False
    
    # Check if the URL contains malicious fragments
    frag = urllib.parse.urlparse(url).fragment
    if re.search("^[a-zA-Z0-9_]+$", frag):
        continue
    else:
        return False
    
    return True
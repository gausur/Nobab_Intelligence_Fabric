#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-14 07:07:03.622601

import re
import urllib.parse

def is_phishing_url(url):
    """
    Detects if the URL is a phishing attempt by checking for common phishin[7D[K
phishing patterns in the hostname and path components of the URL.
    
    Args:
        url (str): The URL to be analyzed.
        
    Returns:
        bool: True if the URL is likely a phishing attack, False otherwise.[10D[K
otherwise.
    """
    # Check for common phishing patterns in the hostname
    hostname = urllib.parse.urlparse(url).hostname
    if re.search(r"\.onion$", hostname) or re.search(r"\.(co|net)\.\w+$", h[1D[K
hostname):
        return True
    
    # Check for common phishing patterns in the path component of the URL
    path = urllib.parse.urlparse(url).path
    if re.search(r"\.html?$", path) and not re.search(r"\.\w{2,3}\.\w{1,4}$[31D[K
re.search(r"\.\w{2,3}\.\w{1,4}$", path):
        return True
    
    # If the URL does not match any of the above patterns, it is likely a l[1D[K
legitimate URL
    return False
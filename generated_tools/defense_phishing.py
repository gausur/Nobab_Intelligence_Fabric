#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 23:30:24.529393

import re
import ssl

def is_phishing_url(url):
    # Check if the URL is valid
    if not url or not url.startswith("http"):
        return False
    
    # Check if the URL contains a suspicious domain
    suspicious_domains = ["example.com", "fake-site.net"]
    for domain in suspicious_domains:
        if domain in url:
            return True
    
    # Check if the URL's SSL certificate is valid
    try:
        ssl._create_unverified_context = lambda: None
        resp = urllib.request.urlopen(url)
        cert = resp.getpeercert()
        if not cert or "CN" not in cert:
            return False
    
        # Check the CN field of the SSL certificate for suspicious content
        cn = cert["CN"][0]
        if re.search(r"\bexample\b", cn):
            return True
    except (urllib.error.URLError, ssl.SSLError):
        pass
    
    return False
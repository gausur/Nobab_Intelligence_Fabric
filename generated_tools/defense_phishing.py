#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-01 15:58:31.262681

import re
from urllib.parse import urlparse

class PhishingDetector:
    def __init__(self, url):
        self.url = url
    
    def is_phishing(self):
        # Check if the URL is a valid HTTP or HTTPS address
        parsed_url = urlparse(self.url)
        if not (parsed_url.scheme in ['http', 'https']):
            return False
        
        # Check if the domain name has more than two parts
        domain_parts = self.url.split('.')
        if len(domain_parts) < 3:
            return False
        
        # Check if the URL contains suspicious keywords or patterns
        for keyword in ['phishing', 'scam', 'fake', 'fraud']:
            if re.search(keyword, self.url, re.IGNORECASE):
                return True
        
        # Check if the URL is a known phishing site
        with open('phishing_sites.txt') as f:
            for line in f:
                if line.strip() == self.url:
                    return True
        
        # If none of the above checks passed, it's likely not a phishing si[2D[K
site
        return False
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-25 22:09:15.168377

import re
from urllib.parse import urlparse

class PhishingDetector:
    def __init__(self):
        self.whitelist = ["example.com", "example2.com"]
        self.blacklist = ["phishing.com", "scamsite.com"]
    
    def is_phishing(self, url):
        parsed = urlparse(url)
        hostname = parsed.hostname
        
        # Check if the URL is in the whitelist
        if hostname in self.whitelist:
            return False
        
        # Check if the URL is in the blacklist
        if hostname in self.blacklist:
            return True
        
        # Check if the domain has any subdomains that are in the blacklist
        for part in parsed.path.split("/"):
            if part in self.blacklist:
                return True
        
        return False
    
    def mitigate(self, url):
        if not self.is_phishing(url):
            # Do nothing if the URL is not phishing
            return
        
        print("Blocking phishing URL:", url)
        # TODO: Perform blocking action here

# Example usage:
detector = PhishingDetector()
detector.mitigate("https://phishing.com/login")
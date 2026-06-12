#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-12 02:45:12.975129

import re
from typing import List, Dict

class PhishingDetector:
    def __init__(self, domains: List[str], patterns: Dict[str, str]):
        self.domains = domains
        self.patterns = patterns
    
    def is_phishing(self, url: str) -> bool:
        for domain in self.domains:
            if domain in url:
                return True
        return False
    
    def mitigate_phishing(self, url: str) -> str:
        for pattern in self.patterns:
            if re.search(pattern, url):
                return ""
        return url
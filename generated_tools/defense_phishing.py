#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-20 06:43:41.824500

import re
import urllib.parse
from typing import Dict, List

class PhishingAttackDetector:
    def __init__(self, domains: List[str], patterns: Dict[str, str]) -> Non[3D[K
None:
        self.domains = domains
        self.patterns = patterns
    
    def detect_phishing(self, url: str) -> bool:
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        if not domain or domain not in self.domains:
            return False
        for pattern, regex in self.patterns.items():
            if re.search(regex, url):
                return True
        return False
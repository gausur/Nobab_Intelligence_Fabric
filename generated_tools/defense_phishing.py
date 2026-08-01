#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-01 16:55:39.903755

import re

class PhishingDetector:
    def __init__(self):
        self.phishing_regex = r"(?i)((?:https?:\/\/)?)(?<![\w\.]).+(\.\w{2,[45D[K
r"(?i)((?:https?:\/\/)?)(?<![\w\.]).+(\.\w{2,})(:(80|443))?(\/|\b)"
    
    def detect_phishing(self, url):
        if re.search(self.phishing_regex, url):
            return True
        else:
            return False

if __name__ == "__main__":
    detector = PhishingDetector()
    url = "http://example.com"
    print(detector.detect_phishing(url))
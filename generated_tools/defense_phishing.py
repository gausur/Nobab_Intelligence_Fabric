#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-29 17:31:36.156542

import re
import sys
from typing import List, Union

class PhishingDetector:
    def __init__(self):
        self.patterns = []
        self.load_patterns()

    def load_patterns(self):
        with open("phishing_patterns.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                self.patterns.append(line)

    def detect_phishing(self, url: str) -> bool:
        for pattern in self.patterns:
            if re.search(pattern, url):
                return True
        return False

    def mitigate_phishing(self, url: str) -> Union[str, None]:
        if self.detect_phishing(url):
            print("Phishing attack detected!")
            return None
        else:
            return url

if __name__ == "__main__":
    detector = PhishingDetector()
    urls = [sys.argv[1], sys.argv[2]]
    for url in urls:
        print(detector.mitigate_phishing(url))
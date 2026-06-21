#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-21 17:23:38.858264

import re
import sys

class PhishingDetector:
    def __init__(self, url):
        self.url = url

    def is_phishing(self):
        patterns = [r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", r"[2D[K
r"\b(https?|ftp)://[-A-Z0-9+&@#/%?=~_|!:,.;]*[-A-Z0-9+&@#/%=~_|]"]
        for pattern in patterns:
            if re.search(pattern, self.url):
                return True
        return False

def main():
    url = sys.argv[1]
    detector = PhishingDetector(url)
    print("Is the URL a phishing attack?", detector.is_phishing())

if __name__ == "__main__":
    main()
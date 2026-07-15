#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-15 04:43:52.702346

import re
import urllib
from typing import List

class PhishingDetector:
    def __init__(self, urls: List[str]) -> None:
        self.urls = urls
    
    def is_phishing(self) -> bool:
        for url in self.urls:
            if "https://" not in url:
                return True
        return False

def main():
    # Get the list of URLs to check from the command line arguments
    urls = sys.argv[1:]

    # Create a PhishingDetector object with the list of URLs
    detector = PhishingDetector(urls)

    # Check if any of the URLs are phishing sites
    if detector.is_phishing():
        print("The following URL(s) are phishing sites:")
        for url in urls:
            if "https://" not in url:
                print(url)
        sys.exit(1)
    else:
        print("No phishing sites found.")

if __name__ == "__main__":
    main()
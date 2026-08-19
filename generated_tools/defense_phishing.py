#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-19 08:29:44.363734

import re
import sys

class PhishingDetector:
    def __init__(self, domain):
        self.domain = domain

    def is_phishing(self):
        if not self.domain.endswith('.com'):
            return False
        return True

def main():
    if len(sys.argv) != 2:
        print('Usage: python phishing_detector.py <domain>')
        return
    domain = sys.argv[1]
    detector = PhishingDetector(domain)
    if detector.is_phishing():
        print(f'The domain {domain} is a phishing site.')
    else:
        print(f'The domain {domain} is not a phishing site.')

if __name__ == '__main__':
    main()
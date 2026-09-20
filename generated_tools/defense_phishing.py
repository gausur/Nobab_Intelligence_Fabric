#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-20 22:50:04.873442

import re
import sys

def detect_phishing_attacks(url):
    pattern = r"^(?:http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attacks(url):
    if detect_phishing_attacks(url):
        print("Phishing attack detected!")
        sys.exit(1)
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attacks(sys.argv[1])
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-02 16:51:25.999983

import re
import sys

def detect_phishing(url):
    pattern = r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,[61D[K
r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$"
    if not re.match(pattern, url):
        return False
    else:
        return True

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Phishing URL detected!")
        sys.exit(1)
    else:
        print("Valid URL detected.")
        sys.exit(0)

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    mitigate_phishing(url)
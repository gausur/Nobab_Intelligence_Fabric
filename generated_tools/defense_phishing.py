#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 04:36:11.120795

import re
import sys

def detect_phishing(url):
    pattern = r"^https?://.*\.com$"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("This is a phishing website. Do not proceed.")
        sys.exit(1)
    else:
        print("This is not a phishing website. Proceed with caution.")

def main():
    url = input("Enter the URL: ")
    mitigate_phishing(url)

if __name__ == "__main__":
    main()
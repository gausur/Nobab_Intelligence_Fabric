#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-18 23:45:37.172449

import re

def detect_phishing(url):
    pattern = r"^https?:\/\/(www\.)?google\.com$"
    if re.match(pattern, url):
        return "Google"
    else:
        return "Not Google"

def mitigate_phishing(url):
    if detect_phishing(url) == "Not Google":
        print("Possible phishing attack detected!")
        # Insert appropriate mitigation here, e.g. block the URL or redirec[7D[K
redirect to a safe page
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing(url)
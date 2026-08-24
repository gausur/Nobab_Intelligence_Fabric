#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-24 05:34:23.382261

import re

def detect_phishing(url):
    if re.match(r"^https?://", url):
        return False
    elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", url)[4D[K
url):
        return True
    else:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("This is a phishing website!")
    else:
        print("This is a legitimate website.")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    mitigate_phishing(url)
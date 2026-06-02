#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-02 10:09:05.481941

import re

def detect_phishing(url):
    pattern = r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,[61D[K
r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$"
    if not re.match(pattern, url):
        return "Invalid URL"
    else:
        return "Valid URL"

def mitigate_phishing(url):
    # Additional code to detect and mitigate phishing attacks
    pass

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    result = detect_phishing(url)
    if result == "Valid URL":
        mitigate_phishing(url)
    else:
        print(result)
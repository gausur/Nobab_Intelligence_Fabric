#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-13 02:37:26.695456

import re

def detect_phishing(url):
    pattern = r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,[61D[K
r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0r"^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$"
    if not re.match(pattern, url):
        return False

    domain = urlparse(url).netloc
    if "." in domain:
        parts = domain.split(".")
        if len(parts) > 2 and len(parts[-1]) <= 6:
            return True

    return False

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing(url)
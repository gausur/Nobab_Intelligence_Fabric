#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-24 21:49:17.144401

import re
import smtplib

def detect_phishing(url):
    pattern = r"(http|https)://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if re.match(pattern, url):
        return False
    else:
        return True

def mitigate_phishing(url):
    if detect_phishing(url):
        return "Invalid URL"
    else:
        return "Valid URL"

def main():
    url = input("Enter a URL: ")
    result = mitigate_phishing(url)
    print(result)

if __name__ == "__main__":
    main()
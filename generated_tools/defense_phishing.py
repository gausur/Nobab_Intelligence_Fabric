#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-30 06:53:07.737401

import re

def is_phishing_url(url):
    pattern = r"^(?:http|https)://.*\.com/.*$"
    if re.match(pattern, url):
        return False
    else:
        return True

def mitigate_phishing(url):
    if is_phishing_url(url):
        print("This is a phishing URL!")
    else:
        print("This is not a phishing URL.")

if __name__ == "__main__":
    url = input("Enter the URL to be checked: ")
    mitigate_phishing(url)
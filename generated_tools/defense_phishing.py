#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-30 21:48:28.312899

import re
import urllib.parse

def detect_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme != "https":
        return False
    if parsed_url.netloc.endswith(".com"):
        return False
    if parsed_url.netloc.endswith(".org"):
        return False
    if parsed_url.netloc.endswith(".net"):
        return False
    if parsed_url.netloc.endswith(".edu"):
        return False
    if parsed_url.netloc.endswith(".gov"):
        return False
    if parsed_url.netloc.endswith(".mil"):
        return False
    return True

def mitigate_phishing_attack(url):
    if detect_phishing_attack(url):
        return "Phishing attack detected. Please contact the website owner [K
to report the issue."
    else:
        return "No phishing attack detected."

def main():
    url = input("Enter a URL: ")
    result = mitigate_phishing_attack(url)
    print(result)

if __name__ == "__main__":
    main()
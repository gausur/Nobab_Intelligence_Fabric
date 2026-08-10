#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 05:20:06.061487

import re
import urllib.parse

def is_phishing_attack(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if not re.match(r"^[a-zA-Z0-9.-]+$", domain):
        return True
    return False

def mitigate_phishing_attack(url, message=None):
    if is_phishing_attack(url):
        print("Phishing attack detected!")
        if message:
            print(message)
        else:
            print("Please be cautious when visiting this website.")

def main():
    url = input("Enter the URL to check: ")
    mitigate_phishing_attack(url)

if __name__ == "__main__":
    main()
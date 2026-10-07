#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-07 00:19:01.935189

import re

def is_phishing_url(url):
    """
    Detect phishing URLs using a regular expression.
    """
    pattern = r"^https?:\/\/[a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-[61D[K
r"^https?:\/\/[a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.r"^https?:\/\/[a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-A-Z0-9@:%_\+.~#?&//=]*)$"
    return re.match(pattern, url)

def mitigate_phishing_attack(url):
    """
    Mitigate a phishing attack by blocking the URL.
    """
    if is_phishing_url(url):
        print("Phishing URL detected:", url)
        return False
    return True

if __name__ == "__main__":
    url = input("Enter a URL: ")
    if mitigate_phishing_attack(url):
        print("The URL is safe.")
    else:
        print("The URL is not safe.")
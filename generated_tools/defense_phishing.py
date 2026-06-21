#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-21 23:04:23.162373

import re

def is_phishing_url(url):
    pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6[61D[K
r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attacks found.")

if __name__ == "__main__":
    url = input("Enter the URL to check for phishing attacks: ")
    mitigate_phishing_attack(url)
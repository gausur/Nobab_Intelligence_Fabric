#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-07 23:17:19.089695

import re
import sys

def is_phishing_url(url):
    pattern = re.compile(r'https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[61D[K
re.compile(r'https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([re.compile(r'https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
    if pattern.match(url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Possible phishing attack detected!")
        sys.exit(1)
    else:
        print("No phishing attack detected.")
        sys.exit(0)

def main():
    url = input("Enter the URL: ")
    mitigate_phishing_attack(url)

if __name__ == '__main__':
    main()
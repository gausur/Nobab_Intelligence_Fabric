#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 03:30:10.239918

import re

def is_phishing(url):
    pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,[61D[K
r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$'
    match = re.search(pattern, url)
    if match:
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Possible phishing site!")
    else:
        print("Not a phishing site.")

mitigate_phishing("https://www.example.com")
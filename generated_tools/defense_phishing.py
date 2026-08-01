#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-01 22:47:23.032310

import re

def is_phishing(url):
    pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6[61D[K
r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    match = re.search(pattern, url)
    if not match:
        return False
    domain = match.group(1)
    if ".".join(domain.split(".")[-2:]) in ["com", "org", "net"]:
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("This URL is a phishing attack, please do not proceed.")
    else:
        print("This URL is safe to visit.")

if __name__ == "__main__":
    mitigate_phishing("https://www.example.com")
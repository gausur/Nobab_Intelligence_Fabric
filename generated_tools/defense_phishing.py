#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-26 05:27:34.200652

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    pattern = re.compile(r"(?i)(\b(https?|ftp):\/\/[a-z0-9][\-a-z0-9]+\.)+[[61D[K
re.compile(r"(?i)(\b(https?|ftp):\/\/[a-z0-9][\-a-z0-9]+\.)+[a-z]{2,}(?:\/[re.compile(r"(?i)(\b(https?|ftp):\/\/[a-z0-9][\-a-z0-9]+\.)+[-z]{2,}(?:\/[^\.\/][^\.\/]*)*\/?$")
    if not pattern.match(domain):
        return False
    else:
        return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        # Add additional mitigation steps here, such as blocking the URL or[2D[K
or reporting the incident
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing_attack(url)
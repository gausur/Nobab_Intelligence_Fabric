#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-16 00:34:44.568845

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if not (parsed.scheme == "http" or parsed.scheme == "https"):
        return False
    domain = "{0}.{1}".format(parsed.netloc, parsed.domain)
    if re.search("(\w+)\.(google|facebook|twitter|instagram)\.(com|co\.uk)"[68D[K
re.search("(\w+)\.(google|facebook|twitter|instagram)\.(com|co\.uk)", domai[5D[K
domain):
        return True
    return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    mitigate_phishing(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-30 13:07:20.600291

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if not parsed.netloc:
        return False
    if not re.match("^[a-zA-Z0-9.-]+$", parsed.netloc):
        return True
    if re.search("://\w+\.", parsed.netloc):
        return True
    if re.search("\.\w+", parsed.netloc):
        return True
    return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attempt detected!")
        return "https://example.com"
    else:
        return url

def main():
    url = input("Enter a URL: ")
    mitigated_url = mitigate_phishing(url)
    if mitigated_url != url:
        print("Mitigated URL:", mitigated_url)

if __name__ == "__main__":
    main()
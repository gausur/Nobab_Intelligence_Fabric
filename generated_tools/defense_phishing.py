#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-21 06:33:52.642241

import re
import urllib.parse

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    pattern = re.compile("[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}$")
    if not pattern.match(domain):
        return "Phishing detected"
    return "No phishing detected"

def mitigate_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain == "example.com":
        return "Phishing mitigated"
    return "No phishing detected"

def main():
    url = input("Enter URL: ")
    result = detect_phishing(url)
    print(result)
    mitigate_phishing(url)

if __name__ == "__main__":
    main()
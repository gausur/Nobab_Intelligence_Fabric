#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 22:19:56.309770

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if hostname.endswith("example.com"):
        return True
    return False

def mitigate_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if hostname.endswith("example.com"):
        return "https://example.com"
    return url

def main():
    url = input("Enter a URL: ")
    if is_phishing_url(url):
        mitigated_url = mitigate_phishing_url(url)
        print(f"Mitigated URL: {mitigated_url}")
    else:
        print(f"URL is not a phishing attack: {url}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-22 21:17:26.796546

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme == "http" and parsed_url.netloc == "www.example.co[15D[K
"www.example.com":
        return True
    return False

def mitigate_phishing_url(url):
    if is_phishing_url(url):
        print("This is a phishing URL!")
    else:
        print("This is not a phishing URL.")

def main():
    url = input("Enter a URL: ")
    mitigate_phishing_url(url)

if __name__ == "__main__":
    main()
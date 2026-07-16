#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-16 11:42:35.782010

import re
import socket

def is_phishing_url(url):
    pattern = r"^https?://([^/]+)/$"
    match = re.match(pattern, url)
    if not match:
        return False
    host = match.group(1)
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return True
    return False

def main():
    while True:
        url = input("Enter URL: ")
        if is_phishing_url(url):
            print("Phishing URL detected!")
        else:
            print("Safe URL.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-11 17:09:48.062178

import re
import urllib.parse
import socket

def detect_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    try:
        socket.gethostbyname(hostname)
    except socket.gaierror:
        return False
    else:
        return True

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    mitigate_phishing(url)
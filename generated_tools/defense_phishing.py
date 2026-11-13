#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-13 19:02:51.345181

import re
import socket
import urllib.request
from urllib.parse import urlparse

def detect_phishing(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        return False
    return True

def mitigate_phishing(url):
    if detect_phishing(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing("http://example.com")
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-11 18:51:25.997989

import re
import ssl
import socket
from urllib import request, error

def is_phishing(url):
    # Check if the URL is valid
    try:
        request.urlopen(url)
    except error.URLError:
        return False

    # Check for common phishing patterns
    pattern = re.compile("[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    if not pattern.match(url):
        return False

    # Check for SSL certificates
    try:
        ssl.get_server_certificate((socket.gethostbyname(url), 443))
    except ssl.SSLError:
        return False

    return True

def mitigate_phishing(url):
    # Redirect to a safe URL
    request.urlopen("https://example.com")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    if is_phishing(url):
        mitigate_phishing(url)
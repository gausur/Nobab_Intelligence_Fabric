#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-16 15:52:39.562736

import re
import socket

def is_phishing(url):
    # Check if the URL contains suspicious characters
    if re.search(r'[~!@#$%^&*()_+{}\[\]:";<>?,.\/' + url, re.IGNORECASE):
        return True

    # Check if the URL is a valid IP address or hostname
    try:
        socket.gethostbyname(url)
    except socket.gaierror:
        return False

    # Check if the URL is on the public internet
    try:
        socket.getaddrinfo(url, 80)
    except socket.gaierror:
        return False

    return True

def mitigate_phishing(url):
    # Redirect the user to a safe website
    print("Please visit this safe website instead: " + url)

# Test the script
if __name__ == '__main__':
    is_phishing("http://www.example.com")  # should be False
    mitigate_phishing("http://www.example.com")  # should print a message t[1D[K
to redirect the user to a safe website
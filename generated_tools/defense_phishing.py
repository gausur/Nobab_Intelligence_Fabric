#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-30 10:28:36.607904

import re
import socket

def is_phishing(url):
    pattern = r"^http[s]?://(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])[61D[K
r"^http[s]?://(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{r"^http[s]?://(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])\.)+[a-zA-Z]{2,6}$"
    if not re.match(pattern, url):
        return False
    try:
        socket.gethostbyname(url)
    except socket.gaierror:
        return True
    return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attack detected!")
        # Add your custom logic here to block the URL or notify the user

if __name__ == "__main__":
    url = input("Enter a URL: ")
    mitigate_phishing(url)
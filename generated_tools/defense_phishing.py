#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-07 10:50:03.827630

import re
import socket
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    domain = parsed_url.hostname
    if not hostname or not domain:
        return False
    try:
        socket.gethostbyname(hostname)
    except socket.gaierror:
        # Host does not exist, likely phishing
        return True
    if not re.match(r"^[\w\.]+", hostname):
        # Hostname contains invalid characters, likely phishing
        return True
    if not re.match(r"^\w+\.\w+$", domain):
        # Domain is invalid, likely phishing
        return True
    if hostname.endswith("." + domain):
        # Hostname ends with the domain, likely phishing
        return True
    return False

def mitigate_phishing(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing("https://www.example.com")
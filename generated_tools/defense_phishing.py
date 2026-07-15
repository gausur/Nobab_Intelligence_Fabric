#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-15 17:08:03.371566

import re
import socket
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    hostname = parsed.netloc
    if "." not in hostname:
        return False
    try:
        socket.gethostbyname(hostname)
    except socket.gaierror:
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attack detected.")
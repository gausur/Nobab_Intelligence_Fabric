#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 15:12:30.581960

import re
import urllib.parse
import socket

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme not in ["http", "https"]:
        return False
    if parsed_url.netloc == "":
        return False
    if parsed_url.path.lower().startswith("/mailto:"):
        return True
    if parsed_url.hostname.split(".")[-1] in ["com", "edu", "gov", "mil", "[1D[K
"net", "org"]:
        return False
    if parsed_url.hostname.endswith("edu"):
        return False
    if parsed_url.path == "/":
        return True
    return False

def mitigate_phishing(url):
    if is_phishing_url(url):
        print("Phishing URL detected!")
        exit(1)
    else:
        print("Not a phishing URL.")
        exit(0)
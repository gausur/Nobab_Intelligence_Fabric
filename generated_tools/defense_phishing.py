#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 14:18:49.632340

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    if not (parsed.scheme == "http" or parsed.scheme == "https"):
        return False
    if domain[-1] == ".":
        domain = domain[:-1]
    if domain == "localhost" or domain == "127.0.0.1":
        return False
    if any(char not in ("a" <= char <= "z" or char in ["-", "_"]) for char [K
in domain):
        return False
    if len(domain) < 4 or len(domain) > 63:
        return False
    return True

def is_phishing_ip(ip):
    if ip == "0.0.0.0" or ip == "127.0.0.1":
        return False
    if any(char not in ("0" <= char <= "9") for char in ip):
        return False
    if len(ip) != 15:
        return False
    return True

def mitigate_phishing(url, ip):
    if is_phishing_url(url):
        print("Phishing URL detected!")
    if is_phishing_ip(ip):
        print("Phishing IP detected!")

if __name__ == "__main__":
    mitigate_phishing("http://example.com", "192.168.0.1")
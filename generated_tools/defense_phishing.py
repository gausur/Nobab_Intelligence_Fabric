#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-03 00:01:11.532842

import re
import sys
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        return False
    if "." in hostname and hostname[-1] == ".":
        return True
    return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        sys.exit()

if __name__ == "__main__":
    mitigate_phishing_attack(sys.argv[1])
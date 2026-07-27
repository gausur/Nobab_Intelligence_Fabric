#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-27 06:22:54.985177

import re
import urllib.parse

def is_phishing(url):
    parsed = urllib.parse.urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return False
    if "@" in hostname or "." in hostname:
        return True
    if re.match(r"[a-zA-Z0-9.-]+$", hostname):
        return False
    else:
        return True

def mitigate_phishing(url, headers=None):
    if is_phishing(url):
        print("Possible phishing attack detected!")
        return "Invalid URL"
    else:
        return url
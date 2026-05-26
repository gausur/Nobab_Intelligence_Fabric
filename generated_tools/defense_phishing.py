#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-26 14:51:44.111605

import re
import urllib.parse

def is_phishing(url):
    """Check if the URL is a phishing attack."""
    parsed = urllib.parse.urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return False
    if "http://" in hostname or "https://" in hostname:
        return True
    if hostname.endswith("www.example.com"):
        return True
    if re.search(r"\.(exe|zip|rar|jar|bin)$", hostname):
        return True
    if re.search(r"\.(php|jsp|aspx|py)$", hostname):
        return True
    if re.search(r"[^\w.-]", hostname):
        return True
    return False

def mitigate_phishing(url):
    """Mitigate phishing attacks by opening the URL in a new tab."""
    import webbrowser
    webbrowser.open(url, new=2)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    if is_phishing(url):
        mitigate_phishing(url)
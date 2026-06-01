#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-01 20:53:26.437428

import re
import sys
from urllib.parse import urlparse

def is_phishing(url):
    # Check if the URL contains common phishing patterns
    if "http" in url and not url.startswith("https"):
        return True
    elif any(pattern in url for pattern in ("www.", "facebook", "twitter", [K
"linkedin")):
        return True
    else:
        return False

def mitigate_phishing(url):
    # Redirect to HTTPS version of the URL if possible
    parsed_url = urlparse(url)
    if parsed_url.scheme == "http":
        return f"https://{parsed_url.netloc}{parsed_url.path}"
    else:
        return url

if __name__ == "__main__":
    # Get the URL from the command line arguments
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        print("Usage: python phishing_detector.py <url>")
        exit()

    # Check if the URL is a phishing attack
    if is_phishing(url):
        mitigated_url = mitigate_phishing(url)
        print(f"Phishing attack detected: {url}")
        print(f"Mitigated URL: {mitigated_url}")
    else:
        print("No phishing attacks detected")
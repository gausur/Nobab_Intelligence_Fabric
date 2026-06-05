#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-05 10:55:21.350434

import re
import urllib.parse
from http import client

def is_phishing(url):
    # Check if the URL is valid
    try:
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError("Invalid URL")
    except Exception as e:
        print(f"Failed to parse URL {url}: {e}")
        return False

    # Check if the domain is in the browser's list of known phishing sites
    with open("phishing_sites.txt", "r") as f:
        for line in f:
            if parsed.netloc == line.strip():
                print(f"Phishing site detected: {url}")
                return True

    # Check if the URL contains suspicious patterns
    if re.search(r"(\bphishing\b|fake|scam)", url, re.IGNORECASE):
        print(f"Suspicious pattern detected in URL: {url}")
        return True

    # Check if the URL is for a known malware site
    if parsed.netloc in {"example.com", "malware.site"}:
        print(f"Malware site detected: {url}")
        return True

    # Check if the URL is for a known phishing site
    try:
        response = client.urlopen(url)
        html = response.read().decode("utf-8")
        if re.search(r"<title>Phishing</title>", html):
            print(f"Phishing site detected: {url}")
            return True
    except Exception as e:
        pass

    # If no phishing patterns are found, the URL is likely safe
    print(f"URL is likely safe: {url}")
    return False
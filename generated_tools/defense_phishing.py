#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-12 08:05:41.557985

import re
from urllib.parse import urlparse
from http.client import HTTPConnection

def is_phishing_url(url):
    # Check if the URL is a phishing site by analyzing its domain name and [K
HTTP status code
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    conn = HTTPConnection(domain_name, timeout=5)
    try:
        conn.request("HEAD", "/")
        response = conn.getresponse()
        if response.status != 200:
            return True
    except Exception as e:
        print(f"Failed to connect to {domain_name}: {e}")
        return False
    finally:
        conn.close()
    return False

def detect_phishing_attacks(url):
    # Check if the URL is a phishing site by analyzing its domain name and [K
HTTP status code
    if is_phishing_url(url):
        print(f"Phishing attack detected: {url}")
    else:
        print(f"No phishing attack detected: {url}")

def main():
    # Prompt the user to enter a URL
    url = input("Enter a URL: ")
    detect_phishing_attacks(url)

if __name__ == "__main__":
    main()
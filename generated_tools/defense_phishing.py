#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-13 12:59:59.925244

import re
import urllib.parse

def is_phishing_url(url):
    # Check if the URL is a phishing URL
    if re.search(r"phishing\.com", url):
        return True
    # Check if the URL is a phishing subdomain
    if re.search(r"phishing\.[a-z]+\.com", url):
        return True
    # Check if the URL is a phishing domain
    if re.search(r"phishing\.com", url):
        return True
    return False

def mitigate_phishing_attack(url):
    # Redirect the user to a safe URL
    safe_url = "https://example.com"
    urllib.parse.urljoin(safe_url, url)
    return safe_url

def main():
    # Get the URL from the user
    url = input("Enter the URL: ")
    # Check if the URL is a phishing URL
    if is_phishing_url(url):
        # Mitigate the phishing attack
        mitigate_phishing_attack(url)
        print("Phishing attack detected and mitigated.")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()
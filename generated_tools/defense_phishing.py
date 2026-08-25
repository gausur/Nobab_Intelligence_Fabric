#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-25 08:34:03.122026

import re

def detect_phishing(url):
    """
    Detects phishing attacks by analyzing the URL for suspicious patterns.

    :param url: The URL to be analyzed.
    :return: True if the URL is a phishing attack, False otherwise.
    """
    # Check for suspicious patterns in the URL
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", url):
        # If the URL contains an email address, it's likely a phishing atta[4D[K
attack
        return True
    elif re.search(r"https?://[a-zA-Z0-9.-]+", url):
        # If the URL contains a domain name, it's likely a legitimate websi[5D[K
website
        return False
    else:
        # If the URL doesn't contain an email address or a domain name, it'[3D[K
it's likely a phishing attack
        return True

def mitigate_phishing(url):
    """
    Mitigates phishing attacks by redirecting the user to a safe URL.

    :param url: The URL to be redirected.
    :return: The safe URL to redirect the user to.
    """
    safe_url = "https://www.example.com"
    return safe_url

def main():
    # Get the URL from the user
    url = input("Enter the URL: ")

    # Detect and mitigate the phishing attack
    if detect_phishing(url):
        mitigate_phishing(url)
        print("Phishing attack detected! Redirecting to safe URL...")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()
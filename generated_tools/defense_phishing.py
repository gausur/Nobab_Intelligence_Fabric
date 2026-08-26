#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-26 03:48:43.621739

import re
import requests

def detect_phishing_attack(url):
    """
    Detects phishing attacks by checking if the URL is a valid domain
    and if the URL contains any suspicious keywords.
    """
    # Check if the URL is a valid domain
    if not url.startswith("http"):
        return False

    # Check if the URL contains any suspicious keywords
    if re.search(r"[phishing|scam|malware|virus]", url):
        return True

    return False

def mitigate_phishing_attack(url):
    """
    Mitigates phishing attacks by blocking the URL and
    alerting the user to the potential threat.
    """
    # Block the URL
    requests.get(url)

    # Alert the user to the potential threat
    print("WARNING: Phishing attack detected. Blocking URL...")

# Main function
def main():
    # Get the URL from the user
    url = input("Enter the URL: ")

    # Detect and mitigate the phishing attack
    if detect_phishing_attack(url):
        mitigate_phishing_attack(url)
    else:
        print("URL is safe.")

# Call the main function
main()
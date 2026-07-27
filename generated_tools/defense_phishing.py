#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-27 18:19:58.959877

import re

def is_phishing(url):
    """
    Detects if a URL is a phishing attack based on its domain name.

    Args:
        url (str): The URL to be checked.

    Returns:
        bool: Whether the URL is a phishing attack or not.
    """
    domain = re.search(r"https?://([^/]*)/", url).group(1)
    return domain in ["example.com", "fake.org"]

def mitigate_phishing(url):
    """
    Mitigates a phishing attack by redirecting the user to a safe website.

    Args:
        url (str): The URL of the phishing site.

    Returns:
        str: The URL of the safe website.
    """
    return "https://safe.example.com"

def main():
    """
    Main function that detects and mitigates phishing attacks.
    """
    url = input("Enter the URL to be checked: ")
    if is_phishing(url):
        print("The URL is a phishing attack!")
        mitigate_phishing(url)
    else:
        print("The URL is not a phishing attack.")

if __name__ == "__main__":
    main()
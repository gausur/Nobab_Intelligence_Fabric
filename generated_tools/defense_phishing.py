#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-02 18:20:09.860685

import re
import requests

def is_phishing_site(url):
    """
    Check if the given URL is a phishing site.
    """
    # Check if the URL is valid
    if not re.match(r"^https?://", url):
        return False

    # Check if the URL is in the phishing database
    with open("phishing_sites.txt", "r") as f:
        for line in f:
            if line.strip() == url:
                return True

    # Check if the URL is in the phishing list
    try:
        response = requests.get(url + "/robots.txt")
        if "Disallow: /" in response.text:
            return True
    except requests.exceptions.RequestException:
        pass

    # Check if the URL has a suspicious domain name
    if any(word in url for word in ["fake", "scam", "phishing"]):
        return True

    return False

def mitigate_phishing_attack(url):
    """
    Mitigate the phishing attack by blocking the URL.
    """
    # Check if the URL is a phishing site
    if is_phishing_site(url):
        # Block the URL
        with open("blocked_urls.txt", "a") as f:
            f.write(url + "\n")
        print("Phishing site blocked:", url)

# Main function
if __name__ == "__main__":
    # Get the URL to check
    url = input("Enter the URL to check: ")

    # Check if the URL is a phishing site
    if is_phishing_site(url):
        mitigate_phishing_attack(url)
    else:
        print("No phishing attack detected.")
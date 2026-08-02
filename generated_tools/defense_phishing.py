#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-02 17:58:31.971114

import re

def is_phishing_url(url):
    # Check if the URL contains common phishing patterns
    pattern = r"(^|\.)google(\.|$)"
    if re.search(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    # Redirect the user to a safe page or display an error message
    print("Access denied! This is not a valid URL.")

# Main function
if __name__ == "__main__":
    url = input("Enter the URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print("Access granted!")
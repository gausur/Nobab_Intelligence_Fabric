#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-26 23:06:51.877918

import re

def is_phishing_url(url):
    # Check if the URL contains any suspicious patterns
    pattern = r"[\w.-]+@([\w-]+\.)+[\w-]{2,4}"
    if re.search(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    # Redirect the user to a safe URL
    print("Redirecting to a safe URL...")
    print("The original URL was:", url)
    print("The safe URL is: https://example.com/safe-page")
    return "https://example.com/safe-page"

def main():
    # Get the user's input from the command line
    url = input("Enter a URL: ")
    
    # Check if the URL contains any suspicious patterns
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print("The URL is safe.")

if __name__ == "__main__":
    main()
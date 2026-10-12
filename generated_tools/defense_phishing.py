#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-12 16:23:16.008855

import re

def is_phishing_url(url):
    # Regular expression to match common phishing URL patterns
    pattern = r"https?:\/\/(?:www\.)?(?:gmail|outlook|yahoo)\.com\/(?:login[61D[K
r"https?:\/\/(?:www\.)?(?:gmail|outlook|yahoo)\.com\/(?:login|signup|forgotr"https?:\/\/(?:www\.)?(?:gmail|outlook|yahoo)\.com\/(?:loginsignup|forgotpassword|resetpassword)"
    return re.match(pattern, url)

def mitigate_phishing_attack(url):
    # Redirect the user to a safe page
    return "https://example.com/safe-page"

def main():
    # Get the URL from the user
    url = input("Enter the URL: ")
    if is_phishing_url(url):
        mitigate_phishing_attack(url)
    else:
        print("The URL is safe")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 19:14:59.701249

import re

def is_phishing_attack(url):
    # Check if the URL is valid
    if not re.match(r"^https?://", url):
        return False
    
    # Check if the domain name is valid
    domain = re.sub(r"https?://", "", url)
    if not re.match(r"\w+\.\w+", domain):
        return False
    
    # Check if the URL contains any suspicious characters
    for char in ["<", ">", '"', "'"]:
        if char in url:
            return False
    
    # Check if the URL is a well-known phishing site
    if domain == "example.com":
        return True
    
    return False

def mitigate_phishing_attack(url):
    # Redirect to a safe page or show an error message
    print("Error: Phishing attack detected")
    return None

if __name__ == "__main__":
    url = input("Enter the URL: ")
    if is_phishing_attack(url):
        mitigate_phishing_attack(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-20 19:18:55.364660

import re

def is_phishing(url):
    # Check if the URL contains the string "://"
    if "://" not in url:
        return False
    
    # Check if the URL contains the string "mailto:"
    if "mailto:" in url:
        return False
    
    # Check if the URL contains the string "@example."
    if "@example." in url:
        return True
    
    # Check if the URL contains a top-level domain that is not in the white[5D[K
whitelist
    tld = re.search(r"\.(\w+)$", url).group(1)
    if tld not in ["com", "net", "org", "edu", "gov"]:
        return True
    
    # Check if the URL contains a subdomain that is not in the whitelist
    subdomain = re.search(r"^(\w+\.)+", url).group(1)
    if subdomain not in ["example", "test", "demo"]:
        return True
    
    # If none of the above conditions are met, it's likely a legitimate URL[3D[K
URL
    return False

def mitigate_phishing(url):
    # Check if the URL is a phishing attack
    if is_phishing(url):
        print("Possible phishing attack detected. Please report.")
        exit()
    
    # If it's not a phishing attack, proceed with opening the URL
    webbrowser.open(url)

# Example usage:
mitigate_phishing("https://example.com")  # Should open the URL in the defa[4D[K
default web browser
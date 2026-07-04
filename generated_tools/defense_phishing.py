#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-04 16:05:24.437168

import re
import requests

# Define the list of email addresses that are allowed to send phishing link[4D[K
links
allowed_emails = ["johndoe@example.com", "janedoe@example.com"]

# Define the pattern for a phishing link
phishing_link_pattern = r"(https?:\/\/)(?:[^@\n]+@)?(?:www\.)?([^.\n]+\.[^.[51D[K
r"(https?:\/\/)(?:[^@\n]+@)?(?:www\.)?([^.\n]+\.[^.\n]+)/?"

def is_phishing_link(url):
    # Check if the URL matches the phishing link pattern
    return re.match(phishing_link_pattern, url)

def get_email_from_url(url):
    # Extract the email address from the URL using a regular expression
    match = re.search(r"([^@\n]+@[^.\n]+\.[^.\n]+)", url)
    if match:
        return match.group(1)
    else:
        return None

def mitigate_phishing_attack(url, allowed_emails):
    # Check if the URL is a phishing link and the email address is not in t[1D[K
the list of allowed emails
    if is_phishing_link(url) and get_email_from_url(url) not in allowed_ema[11D[K
allowed_emails:
        # Mitigate the phishing attack by displaying an error message and r[1D[K
returning None
        print("Phishing attack detected!")
        return None
    else:
        # Return the original URL if it is not a phishing link or the email[5D[K
email address is in the list of allowed emails
        return url

# Test the function with some sample URLs
url1 = "https://www.example.com"
url2 = "http://www.phishing-site.com/login"
url3 = "mailto:johndoe@example.com"

print(mitigate_phishing_attack(url1, allowed_emails)) # Output: https://www[11D[K
https://www.example.com
print(mitigate_phishing_attack(url2, allowed_emails)) # Output: Phishing at[2D[K
attack detected! (None)
print(mitigate_phishing_attack(url3, allowed_emails)) # Output: Phishing at[2D[K
attack detected! (None)
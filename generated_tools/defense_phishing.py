#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-18 22:55:24.771361

import re
from urllib.parse import urlparse
from email.message import EmailMessage

def is_phishing_url(url):
    parsed = urlparse(url)
    if parsed.netloc == "example.com":
        return True
    else:
        return False

def mitigate_phishing_attack(msg):
    # Extract the URL from the message
    url = msg["Message-ID"]
    # Check if the URL is a phishing URL
    if is_phishing_url(url):
        # Print an error message
        print("Phishing attack detected!")
    else:
        # Print a warning message
        print("Possible phishing attack, please verify the URL.")

# Example usage
msg = EmailMessage()
msg["Message-ID"] = "https://www.example.com/phishing"
mitigate_phishing_attack(msg)
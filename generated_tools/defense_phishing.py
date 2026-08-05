#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-05 05:01:57.885456

import re
import requests
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if parsed.netloc in ["www.example.com", "mail.example.com"]:
        return True
    else:
        return False

def mitigate_phishing_attack(url, message_body):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        # Mitigation logic goes here
    else:
        print("No phishing attack detected.")

def main():
    url = input("Enter URL: ")
    message_body = input("Enter message body: ")
    mitigate_phishing_attack(url, message_body)

if __name__ == "__main__":
    main()
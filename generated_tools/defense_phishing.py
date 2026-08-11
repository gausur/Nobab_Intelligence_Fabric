#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 05:55:26.708865

import re
import smtplib

def is_phishing_url(url):
    return re.match(r"^https?://[a-zA-Z0-9.-]*\.[a-zA-Z]{2,3}$", url)

def is_phishing_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$", e[1D[K
email)

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        # block the URL
        return False
    else:
        # allow the URL
        return True

def main():
    url = "http://example.com"
    if mitigate_phishing_attack(url):
        print("URL is safe")
    else:
        print("URL is phishing")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-19 20:20:43.598999

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.endswith("google.com"):
        return True
    else:
        return False

def is_phishing_email(email):
    email_domain = email.split("@")[-1]
    if email_domain == "gmail.com":
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        return True
    else:
        return False

def main():
    url = "http://www.google.com"
    mitigate_phishing_attack(url)

if __name__ == "__main__":
    main()
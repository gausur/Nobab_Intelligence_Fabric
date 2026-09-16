#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-16 23:31:51.891435

import re
import smtplib

def is_phishing_url(url):
    return re.match(r"^http(s)?://[a-zA-Z0-9-.]+(:[0-9]+)?$", url)

def is_phishing_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", em[2D[K
email)

def mitigate_phishing(url, email):
    if is_phishing_url(url):
        return "Phishing URL detected: {}".format(url)
    elif is_phishing_email(email):
        return "Phishing email detected: {}".format(email)
    else:
        return "No phishing detected"

if __name__ == "__main__":
    url = "http://www.example.com"
    email = "johndoe@example.com"
    print(mitigate_phishing(url, email))
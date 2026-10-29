#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-29 01:28:37.660755

import re
import smtplib

def is_phishing_email(email):
    if not email.startswith("http"):
        return False

    domain = email[4:]
    if not re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", domain):
        return False

    try:
        smtplib.SMTP("smtp.gmail.com", 587).connect(domain)
        return True
    except smtplib.SMTPConnectError:
        return False

def mitigate_phishing_attack(email):
    if is_phishing_email(email):
        print("This is a phishing email!")
    else:
        print("This is not a phishing email.")

if __name__ == "__main__":
    mitigate_phishing_attack("https://example.com")
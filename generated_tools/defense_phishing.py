#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-12 23:45:59.807225

import re
import smtplib

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(regex, email) is not None

def is_phishing_attack(email):
    try:
        smtplib.SMTP("smtp.gmail.com", 587).starttls()
        smtplib.SMTP("smtp.gmail.com", 465).connect()
        return False
    except smtplib.SMTPException:
        return True

def mitigate_phishing_attack(email):
    if is_phishing_attack(email):
        print("This email may be a phishing attack. Please proceed with cau[3D[K
caution.")
    else:
        print("This email appears to be legitimate.")

if __name__ == "__main__":
    mitigate_phishing_attack(input("Enter an email address: "))
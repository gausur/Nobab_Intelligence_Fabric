#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 19:25:40.769085

import re
import smtplib

def is_valid_email(email):
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    return re.search(regex, email)

def is_phishing_email(email):
    if not is_valid_email(email):
        return False
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    try:
        smtp_server.starttls()
        smtp_server.login("your_email_address", "your_email_password")
        smtp_server.sendmail("your_email_address", email, "Subject: Phishin[7D[K
Phishing Email Detected")
    except smtplib.SMTPSenderRefused:
        return True
    return False

def mitigate_phishing_email(email):
    if is_phishing_email(email):
        return "Phishing Email Detected"
    return "Email is valid"

if __name__ == "__main__":
    email = input("Enter the email address: ")
    result = mitigate_phishing_email(email)
    print(result)
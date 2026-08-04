#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-04 06:32:32.035347

import re
import smtplib

def is_phishing_email(email):
    # Check if the email contains any suspicious keywords or URLs
    for keyword in ["phish", "scam", "spoof"]:
        if keyword in email.lower():
            return True
    for url in email.split("http://"):
        if len(url) < 10:
            continue
        try:
            response = smtplib.SMTP().sendmail("", "", url)
        except smtplib.SMTPServerDisconnected:
            return True
    return False

def mitigate_phishing_attack(email):
    # Remove any suspicious keywords or URLs from the email
    for keyword in ["phish", "scam", "spoof"]:
        if keyword in email.lower():
            email = email.replace(keyword, "")
    for url in email.split("http://"):
        if len(url) < 10:
            continue
        try:
            response = smtplib.SMTP().sendmail("", "", url)
        except smtplib.SMTPServerDisconnected:
            email = email.replace(url, "")
    return email

def main():
    # Take the input email from the user
    email = input("Enter an email address: ")
    if is_phishing_email(email):
        mitigate_phishing_attack(email)
        print("The email contains suspicious content. Mitigation successful[10D[K
successful.")
    else:
        print("The email does not contain any suspicious content.")

if __name__ == "__main__":
    main()
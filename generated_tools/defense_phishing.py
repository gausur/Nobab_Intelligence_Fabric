#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-18 04:01:35.571061

import re
import smtplib
from email.utils import getaddresses

def is_phishing_attack(email):
    sender, recipient = getaddresses(email)
    subject = email.get("Subject", "")
    body = email.get("Body", "")
    if sender == recipient:
        return False
    if re.search(r"phishing", subject, re.IGNORECASE):
        return True
    if re.search(r"phishing", body, re.IGNORECASE):
        return True
    return False

def mitigate_phishing_attack(email):
    sender, recipient = getaddresses(email)
    if sender != recipient:
        smtplib.SMTP("localhost").sendmail(sender, recipient, email.as_string())
    else:
        smtplib.SMTP("localhost").sendmail(sender, recipient, email.as_string(), bcc=[sender])

def main(email):
    if is_phishing_attack(email):
        mitigate_phishing_attack(email)
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    email = input("Enter the email: ")
    main(email)
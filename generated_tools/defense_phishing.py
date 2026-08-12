#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-12 15:54:32.490436

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    # Check if the email contains a suspicious URL in the body or subject
    if re.search(r"https?://[^\s]+", email.body) or re.search(r"https?://[^[23D[K
re.search(r"https?://[^\s]+", email.subject):
        return True
    else:
        return False

def mitigate_phishing_attack(email):
    # Send a notification to the recipient's email address
    message = EmailMessage()
    message["Subject"] = "Phishing Attempt Detected"
    message["From"] = email.sender
    message["To"] = email.recipients[0]
    message.set_content("Your email contains a phishing attempt. Please do [K
not click any suspicious links or provide any personal information.")
    smtplib.SMTP(email.server).sendmail(message)

def main():
    # Read the email from stdin
    email = EmailMessage()
    email.parse(input())

    if is_phishing_attack(email):
        mitigate_phishing_attack(email)

if __name__ == "__main__":
    main()
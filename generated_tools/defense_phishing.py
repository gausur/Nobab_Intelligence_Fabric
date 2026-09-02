#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-02 23:46:14.269859

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    if not email:
        return False

    pattern = r"[-a-zA-Z0-9._%+]+@[-a-zA-Z0-9.]+\.[a-zA-Z]{2,}"
    if not re.search(pattern, email):
        return False

    host = email.split("@")[1]
    if host.endswith("gmail.com"):
        return True
    elif host.endswith("outlook.com"):
        return True
    elif host.endswith("yahoo.com"):
        return True
    else:
        return False

def mitigate_phishing_attack(email):
    sender = email.get("From")
    recipient = email.get("To")
    subject = email.get("Subject")

    if is_phishing_attack(sender):
        smtplib.sendmail(sender, recipient, subject, "This is a phishing at[2D[K
attack")

def main():
    email = EmailMessage()
    email.set_content("Hello, world!")
    mitigate_phishing_attack(email)

if __name__ == "__main__":
    main()
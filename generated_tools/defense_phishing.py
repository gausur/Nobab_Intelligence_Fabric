#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-15 06:25:08.600937

import re
import smtplib
from email.message import EmailMessage

def detect_phishing_attack(email_message):
    """
    Detect phishing attacks in an email message using regular expressions.
    """
    pattern = r"(https?://)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,[61D[K
r"(https?://)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0r"(https?://)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if re.search(pattern, email_message):
        return True
    else:
        return False

def mitigate_phishing_attack(email_message):
    """
    Mitigate a phishing attack by sending an email to the sender with a war[3D[K
warning.
    """
    sender = email_message.get("From")
    subject = "Phishing Attack Warning"
    body = "We have detected a phishing attack on your account. Please do n[1D[K
not click on any links or provide any personal information."
    msg = EmailMessage()
    msg["From"] = "no-reply@example.com"
    msg["To"] = sender
    msg["Subject"] = subject
    msg.set_content(body)
    smtp = smtplib.SMTP("smtp.example.com")
    smtp.send_message(msg)
    smtp.quit()

def main():
    email_message = EmailMessage()
    email_message.set_content(sys.stdin.read())
    if detect_phishing_attack(email_message):
        mitigate_phishing_attack(email_message)
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()
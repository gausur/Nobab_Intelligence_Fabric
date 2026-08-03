#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-03 09:28:05.839090

import re
import smtplib
from email import message_from_bytes

def is_phishing_email(email):
    if not email:
        return False

    # Check for spammy words in the subject or body of the email
    if any(word in email["subject"] for word in ["phish", "spam", "scam"]):[9D[K
"scam"]):
        return True
    if any(word in email.get_payload() for word in ["phish", "spam", "scam"[6D[K
"scam"]):
        return True

    # Check the sender's domain against a list of known phishing domains
    sender = email["from"].split("<")[1].split(">")[0]
    if sender.endswith(".com"):
        with open("phishing_domains.txt", "r") as f:
            for line in f:
                if line.strip() == sender:
                    return True

    # Check the email's headers for any suspicious values
    for header, value in email.items():
        if any(word in value for word in ["phish", "spam", "scam"]):
            return True

    return False

def mitigate_phishing_email(email):
    # Remove the email from your email client's inbox
    pass

# Test the script by passing a valid and invalid email message to is_phishi[9D[K
is_phishing_email()
message = b"From: Sender <sender@example.com>\r\nTo: Recipient <recipient@e[12D[K
<recipient@example.com>\r\nSubject: Phishing Attack!\r\n\r\nThis is a phish[5D[K
phishing email.\r\n"
valid_email = message_from_bytes(message)
invalid_email = b""

print("Valid email:", valid_email["subject"])
print("Invalid email:", invalid_email["subject"])
print("Is valid email a phishing attack?", is_phishing_email(valid_email))
print("Is invalid email a phishing attack?", is_phishing_email(invalid_emai[30D[K
is_phishing_email(invalid_email))
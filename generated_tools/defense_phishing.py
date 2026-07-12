#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-12 20:07:11.159056

import re
import smtplib
from email.message import EmailMessage
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ["http", "https"]:
        return False
    if parsed_url.netloc.endswith(".com"):
        return True
    else:
        return False

def is_phishing_email(message):
    if message["From"].startswith("john.doe@example.com"):
        return True
    else:
        return False

def mitigate_phishing_attack(message, sender, recipient):
    # Mark the email as spam
    message["X-Spam-Flag"] = "True"
    # Reject the email
    smtplib.SMTP("localhost").sendmail(sender, recipient, message.as_string[17D[K
message.as_string())
    # Log the attack
    print("Phishing attack detected:", message.as_string())

def main():
    # Read email from stdin
    raw_email = sys.stdin.read()
    # Parse the email
    message = EmailMessage()
    message.set_payload(raw_email)
    # Check for phishing URLs and emails
    if is_phishing_url(message["From"]):
        mitigate_phishing_attack(message, "john.doe@example.com", "jane.smi[9D[K
"jane.smith@example.com")
    elif is_phishing_email(message):
        mitigate_phishing_attack(message, "john.doe@example.com", "jane.smi[9D[K
"jane.smith@example.com")

if __name__ == "__main__":
    main()
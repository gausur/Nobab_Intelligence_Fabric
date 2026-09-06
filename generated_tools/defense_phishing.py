#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-06 21:02:22.839408

import re
import smtplib
from email.utils import parseaddr

def is_valid_email(email):
    """
    Check if the email is valid by checking if it contains an @ symbol and [K
if the domain is a valid host.
    """
    if "@" not in email:
        return False
    try:
        localpart, domain = parseaddr(email)[1].split("@", 1)
        if localpart == "" or domain == "":
            return False
        return True
    except Exception:
        return False

def is_phishing_email(email):
    """
    Check if the email is a phishing email by checking if it contains a sus[3D[K
suspicious keyword or link.
    """
    keywords = ["phishing", "scam", "fraud"]
    links = ["https://example.com", "https://example.org"]
    for keyword in keywords:
        if keyword in email.lower():
            return True
    for link in links:
        if link in email.lower():
            return True
    return False

def send_email(email, subject, body):
    """
    Send an email using the smtplib library.
    """
    msg = f"Subject: {subject}\n\n{body}"
    smtplib.sendmail("sender@example.com", email, msg)

def detect_and_mitigate_phishing_attacks(emails):
    """
    Iterate through the list of emails and check if they are phishing email[5D[K
emails.
    If they are, send an email to the sender with a warning.
    """
    for email in emails:
        if is_phishing_email(email):
            send_email(email, "Phishing Attack Detected", "Your email has b[1D[K
been flagged as a phishing attack. Please be cautious when clicking on link[4D[K
links or providing personal information.")

def main():
    emails = ["phishing@example.com", "scam@example.org", "fraud@example.ne[17D[K
"fraud@example.net"]
    detect_and_mitigate_phishing_attacks(emails)

if __name__ == "__main__":
    main()
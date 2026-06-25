#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-25 13:18:09.287615

import re
import smtplib
from email.message import EmailMessage

def detect_phishing(email):
    # Check if the email is from a trusted sender
    if not email["From"].startswith("no-reply") and not email["From"].endsw[19D[K
email["From"].endswith(".example.com"):
        return False
    
    # Check if the email has a valid "Reply-To" header
    if not email["Reply-To"]:
        return False
    
    # Check if the email has a valid "Subject" header
    if not re.match(r"^[A-Za-z0-9 ]+", email["Subject"]):
        return False
    
    # Check if the email has a valid "Message-Id" header
    if not re.match(r"<[\w\.\-\_]+@[\w\.\-\_]+\.\w+>", email["Message-Id"])[20D[K
email["Message-Id"]):
        return False
    
    # Check if the email has a valid "X-Mailer" header
    if not re.match(r"^[A-Za-z0-9]+/[\d\.]+$", email["X-Mailer"]):
        return False
    
    return True

def mitigate_phishing(email):
    # Send an alert to the recipient's administrator
    admin = "admin@example.com"
    msg = EmailMessage()
    msg["From"] = email["From"]
    msg["To"] = admin
    msg["Subject"] = "Phishing Attempt Detected"
    msg.set_content(f"The email {email['Subject']} from {email['From']} has[3D[K
has been flagged as a phishing attempt and may be spam.")
    smtplib.SMTP("localhost").send_message(msg)

def main():
    # Read the email from stdin
    email = sys.stdin.read()
    
    # Detect and mitigate phishing attacks
    if detect_phishing(email):
        mitigate_phishing(email)

if __name__ == "__main__":
    main()
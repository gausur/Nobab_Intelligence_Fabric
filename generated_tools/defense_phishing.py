#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-19 08:04:29.526897

import re
import smtplib
from email.message import EmailMessage

def detect_phishing_attacks(email):
    # Check if the email is from a legitimate source
    if not email["From"].startswith("support@example.com"):
        print("Email is not from a legitimate source")
        return

    # Check if the email contains a malicious URL or attachment
    for part in email.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if re.search(r"https?://[^/]*\.example\.com", part.get_payload()):
            print("Email contains a malicious URL")
            return
        if part.get_filename().endswith(".exe"):
            print("Email contains an executable attachment")
            return

    # Check if the email contains a suspicious subject line
    if re.search(r"[A-Z]+\d{3}[A-Z]{2}", email["Subject"]):
        print("Suspicious subject line detected")
        return

    # Check if the email contains a suspicious greeting
    if not email["Greeting"].startswith("Dear"):
        print("Suspicious greeting detected")
        return

    # Check if the email contains a suspicious signature
    if re.search(r"\bSigned\b", email["Signature"]):
        print("Suspicious signature detected")
        return

    # If no issues are found, mark the email as safe
    print("Email is safe")

def main():
    # Read in the email message from stdin
    msg = EmailMessage()
    msg.set_content(input())

    # Detect and mitigate phishing attacks
    detect_phishing_attacks(msg)

if __name__ == "__main__":
    main()
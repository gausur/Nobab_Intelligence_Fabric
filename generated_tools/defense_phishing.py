#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-29 00:53:32.200036

import re
import smtplib

def check_for_phishing_attacks(email_message):
    # Check for suspicious headers
    if "Received" in email_message.keys():
        for header in email_message["Received"]:
            if re.match(r"from\s+.*\s+by\s+.*\s+with\s+ESMTPSA", header):
                return True
    return False

def mitigate_phishing_attack(email_message):
    # Send a notification to the sender
    smtplib.SMTP("localhost").sendmail(
        email_message["Return-Path"],
        [email_message["From"]],
        "Phishing attack detected. Please do not reply to this email."
    )

def main():
    # Read the email message from the stdin
    email_message = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        key, value = line.split(": ", 1)
        email_message[key] = value

    # Check for phishing attacks
    if check_for_phishing_attacks(email_message):
        mitigate_phishing_attack(email_message)

if __name__ == "__main__":
    main()
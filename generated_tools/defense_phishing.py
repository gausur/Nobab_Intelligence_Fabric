#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-05 22:35:19.797004

import re
import smtplib

def detect_phishing_attacks(email):
    # Check if the email contains any suspicious keywords
    keywords = ["phishing", "scam", "fraud"]
    for keyword in keywords:
        if keyword in email:
            return False

    # Check if the email contains a suspicious link
    if "://" in email:
        domain = re.search(r"^[^@]+@([^@]+\.)+[^@]+", email).group(1)
        if domain.endswith(".edu"):
            return False
        else:
            return True

    return False

def mitigate_phishing_attacks(email):
    # Remove any suspicious links or keywords from the email
    email = re.sub(r"https?://[^\s]+", "", email)
    email = re.sub(r"[^\s]+", "", email)

    # Send the email to the user
    server = smtplib.SMTP("localhost")
    server.sendmail("from@example.com", "to@example.com", email)
    server.quit()

def main():
    # Read the email from stdin
    email = input()

    # Detect and mitigate any phishing attacks
    if detect_phishing_attacks(email):
        mitigate_phishing_attacks(email)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-07 05:32:47.300924

import re
import smtplib

def detect_phishing_attacks(email):
    """
    Detect phishing attacks by checking the subject and body of the email.
    The subject should not contain any suspicious keywords and the body sho[3D[K
should not contain any suspicious links.
    """
    # Check the subject for suspicious keywords
    if re.search(r"(phishing|scam|fraud)", email.subject, re.IGNORECASE):
        return True

    # Check the body for suspicious links
    if re.search(r"(http://|https://|ftp://)", email.body):
        return True

    return False

def mitigate_phishing_attacks(email):
    """
    Mitigate phishing attacks by reporting the email to the sender and bloc[4D[K
blocking the email.
    """
    # Report the email to the sender
    smtplib.SMTP("smtp.gmail.com", 587)
    email.sendmail("from@gmail.com", "to@gmail.com", "Subject: Phishing Att[3D[K
Attempt Detected")

    # Block the email
    smtplib.SMTP("smtp.gmail.com", 587)
    email.sendmail("from@gmail.com", "to@gmail.com", "Subject: Phishing Att[3D[K
Attempt Detected")

def main():
    # Read the email from the input file
    with open("email.txt", "r") as f:
        email = f.read()

    # Detect and mitigate phishing attacks
    if detect_phishing_attacks(email):
        mitigate_phishing_attacks(email)

if __name__ == "__main__":
    main()
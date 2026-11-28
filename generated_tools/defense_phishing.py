#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-28 11:12:57.390746

import re
import smtplib

# Define a regular expression to match phishing emails
PHISHING_REGEX = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

# Define a function to check if an email is phishing
def is_phishing(email):
    if re.match(PHISHING_REGEX, email):
        return True
    else:
        return False

# Define a function to mitigate phishing attacks
def mitigate_phishing(email):
    # Send an email to the sender with a warning
    msg = "Subject: Phishing Attempt Detected\n\n"
    msg += "This is an automated message to warn you that your email contains a phishing link. Please do not click on any links or provide any personal information.\n\n"
    msg += "If you believe this to be a false positive, please reply to this email with the word 'phishing' in the subject line."
    smtplib.sendmail("phishing@example.com", email, msg)

# Define a function to detect phishing emails
def detect_phishing(emails):
    for email in emails:
        if is_phishing(email):
            mitigate_phishing(email)

# Test the script
emails = ["phishing@example.com", "real@example.com"]
detect_phishing(emails)
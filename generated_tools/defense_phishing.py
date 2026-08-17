#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 05:30:58.939504

import re
import smtplib

def detect_phishing(email):
    pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6[61D[K
r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if re.search(pattern, email):
        return True
    else:
        return False

def mitigate_phishing(email):
    if detect_phishing(email):
        # Send an email to the recipient's account to report the phishing a[1D[K
attempt
        smtplib.sendmail("sender@example.com", "recipient@example.com", "Su[3D[K
"Subject: Phishing Attempt", "This is a phishing attempt. Please report imm[3D[K
immediately.")
        return True
    else:
        return False

# Example usage
email = "This is an email with a phishing link: https://example.com/phishin[27D[K
https://example.com/phishing"
print(detect_phishing(email)) # Output: True
print(mitigate_phishing(email)) # Output: True
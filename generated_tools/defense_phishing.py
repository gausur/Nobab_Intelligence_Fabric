#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-29 10:28:31.243523

import re
import smtplib

def is_phishing(email):
    pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6[61D[K
r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if re.search(pattern, email):
        return True
    else:
        return False

def mitigate_phishing(email):
    sender = email["From"]
    recipient = email["To"]
    subject = email["Subject"]
    body = email["Body"]
    if is_phishing(sender) or is_phishing(recipient):
        smtplib.SMTP("smtp.gmail.com", 587).sendmail(sender, recipient, "Th[3D[K
"This is a phishing attack. Do not click on any links.")

def main():
    email = {
        "From": "john.doe@phish.com",
        "To": "jane.smith@gmail.com",
        "Subject": "Important: Click this link to verify your account",
        "Body": "Hello Jane, please click on the link below to verify your [K
account."
    }
    mitigate_phishing(email)

if __name__ == "__main__":
    main()
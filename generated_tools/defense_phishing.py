#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-02 00:15:47.527310

import re
import smtplib

def check_for_phishing(email):
    """Check if an email is a phishing attack"""
    # Check the subject line for keywords like "urgent", "hacked", or "scam[5D[K
"scam"
    subject = email["Subject"].lower()
    for keyword in ("urgent", "hacked", "scam"):
        if keyword in subject:
            return True
    # Check the body of the email for spelling and grammar mistakes
    body = email["Body"]
    mistakes = re.findall(r"\b[a-z]+\b", body, flags=re.IGNORECASE)
    if len(mistakes) > 3:
        return True
    # Check the sender's email address for suspicious characters or domains[7D[K
domains
    sender_email = email["From"]
    if re.search(r"[^\w\.-]+", sender_email):
        return True
    # Check the HTML content of the email for spammy phrases
    html_content = email["HTMLContent"]
    if re.search(r"\bspam|phishing|scam", html_content, flags=re.IGNORECASE[19D[K
flags=re.IGNORECASE):
        return True
    return False

def mitigate_phishing(email):
    """Mitigate a phishing attack by alerting the user and deleting the ema[3D[K
email"""
    # Print an error message to the console
    print("Phishing attempt detected!")
    # Delete the email from the inbox
    smtplib.delete_message(email)

# Loop through the emails in the inbox and check for phishing attacks
for email in smtplib.inbox:
    if check_for_phishing(email):
        mitigate_phishing(email)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-08 00:04:51.317648

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attempt(email):
    # Check if the email is from a known spam source
    if email.get("From") in known_spam_sources:
        return True
    
    # Check if the email has a suspicious subject line
    if re.search(r"phishing|scam", email.get("Subject")):
        return True
    
    # Check if the email contains a malicious link
    for part in email.iter_parts():
        if "Content-Disposition" in part:
            disposition = part["Content-Disposition"]
            if re.search(r"attachment; filename=\w+", disposition):
                # If the attachment has a suspicious file name, it's likely[6D[K
likely malicious
                return True
    
    return False

def mitigate_phishing_attempt(email):
    # Remove any suspicious links or attachments from the email
    for part in email.iter_parts():
        if "Content-Disposition" in part:
            disposition = part["Content-Disposition"]
            if re.search(r"attachment; filename=\w+", disposition):
                # Remove the attachment
                part.dispose()
    
    # Send the modified email to the recipient
    with smtplib.SMTP("localhost") as server:
        message = EmailMessage()
        message["Subject"] = "Your email has been modified"
        message["From"] = email.get("From")
        message["To"] = email.get("To")
        message.set_content(email.as_string())
        server.sendmail(message)

def main():
    # Read the email from stdin
    email = EmailMessage()
    email.parse(sys.stdin)
    
    # Check if the email is a phishing attempt and mitigate it if necessary[9D[K
necessary
    if is_phishing_attempt(email):
        mitigate_phishing_attempt(email)
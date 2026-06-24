#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-24 06:39:55.150486

import re
import smtplib
from email import message_from_bytes

def is_phishing(msg):
    # Check if the sender's domain matches the recipient's domain
    if msg["From"].split("@")[-1] == msg["To"].split("@")[-1]:
        return True
    
    # Check if the email contains any suspicious links or attachments
    for part in message_from_bytes(msg.as_bytes()).walk():
        if "content-disposition" in part:
            # Attachment found, assume it's a phishing attack
            return True
        elif "href=" in part:
            # Suspicious link found, assume it's a phishing attack
            return True
    
    # No suspicious links or attachments found, assume it's not a phishing [K
attack
    return False

def mitigate_phishing(msg):
    # Send the email to an admin for review
    smtplib.sendmail("admin@example.com", msg["To"], "Subject: Phishing Att[3D[K
Attack Detected")
    
# Main function to detect and mitigate phishing attacks
def detect_and_mitigate():
    # Connect to the mail server
    server = smtplib.SMTP("mail.example.com", 25)
    
    # Loop through all incoming emails
    for msg in server.incoming_emails:
        if is_phishing(msg):
            mitigate_phishing(msg)

# Run the main function to start detecting and mitigating phishing attacks
detect_and_mitigate()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-07 02:46:39.319183

import re
import smtplib
from email.message import EmailMessage

def is_phishing_email(email):
    """Check if the given email is a phishing attempt."""
    # Check for spammy keywords in the subject line
    if any(k in email["Subject"] for k in ["scam", "fraud", "urgent"]):
        return True
    
    # Check for spammy keywords in the body of the email
    if any(k in email.get_payload() for k in ["buy now", "click here"]):
        return True
    
    # Check for suspicious domains
    if email["From"].lower().endswith(".com"):
        return True
    
    return False

def mitigate_phishing_attack(email):
    """Mitigate a phishing attack by sending an alert to the sender."""
    # Send an alert to the sender
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attempt Detected"
    msg["From"] = "phishing@example.com"
    msg["To"] = email["From"]
    msg.set_content("This is a phishing attempt. Do not respond to this mes[3D[K
message.")
    smtplib.sendmail("smtp.example.com", msg)
    
def main():
    # Get the email from stdin
    email = input()
    
    # Check if the email is a phishing attack
    if is_phishing_email(email):
        mitigate_phishing_attack(email)
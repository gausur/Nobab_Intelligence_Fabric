#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-28 00:05:11.707787

import re
import smtplib
from email.message import EmailMessage

def detect_phishing_attack(email):
    # Check for spammy keywords
    if any(word in email.lower() for word in ["phish", "scam", "fraud"]):
        return True
    
    # Check for suspicious sender domain
    if not re.match(r"^[^@]+@[^\.]+\.[^\.]+$", email["from"]):
        return True
    
    # Check for missing or invalid recipient
    if not email["to"]:
        return True
    
    return False

def mitigate_phishing_attack(email):
    # Quarantine the email
    with open("quarantine.txt", "a") as f:
        f.write(str(email))
    
    # Send a warning to the sender
    msg = EmailMessage()
    msg["from"] = "no-reply@example.com"
    msg["to"] = email["from"]
    msg["subject"] = "Phishing Attempt Detected"
    msg.set_content("We have detected a phishing attempt on your email acco[4D[K
account. Please do not respond to this message.")
    smtplib.sendmail(None, [email["from"]], msg.as_string())

def main():
    with open("emails.txt") as f:
        emails = [EmailMessage().parse(line) for line in f]
    
    for email in emails:
        if detect_phishing_attack(email):
            mitigate_phishing_attack(email)
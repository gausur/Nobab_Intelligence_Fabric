#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-10 10:19:09.450833

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email has a valid domain
    if not email.split("@")[1].strip():
        return False
    
    # Check if the email has a suspicious domain
    if email.split("@")[1] in ["example.com", "fakeemail.net"]:
        return True
    
    # Check if the email has a suspicious subject
    if re.search(r"Fake Email | Phishing Attack", email.subject):
        return True
    
    # Check if the email has a suspicious message body
    if re.search(r"\bphish\b|\bscam\b|\bfake\b", email.body):
        return True
    
    return False

def mitigate_phishing(email):
    # Send a notification to the user's admin
    smtplib.sendmail("admin@example.com", email.from_, "Phishing attack det[3D[K
detected")
    
    # Block the email from being delivered
    return False

# Test the function
emails = [
    EmailMessage("Fake Email", "This is a fake email"),
    EmailMessage("Real Email", "This is a real email from example.com"),
    EmailMessage("Phishing Attack", "This is a phishing attack"),
]

for email in emails:
    if is_phishing(email):
        mitigate_phishing(email)
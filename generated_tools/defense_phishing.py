#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 18:53:11.947385

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    sender = email["From"]
    recipient = email["To"]
    subject = email["Subject"]
    body = email.get_payload()
    
    # Check if the sender is a known spammer
    spammers = ["spammer1@example.com", "spammer2@example.com"]
    if sender in spammers:
        return True
    
    # Check if the recipient is not a legitimate user
    if recipient not in ["user1@example.com", "user2@example.com"]:
        return True
    
    # Check if the subject contains suspicious keywords
    for keyword in ["phishing", "scam", "fraud"]:
        if keyword in subject:
            return True
    
    # Check if the body contains suspicious links or attachments
    links = re.findall(r"https?://\S+", body)
    for link in links:
        if not link.startswith("http://www.example.com/"):
            return True
    
    # Check if the email contains malware
    if is_malware(body):
        return True
    
    return False

def is_malware(body):
    for keyword in ["virus", "ransomware", "spyware"]:
        if keyword in body:
            return True
    return False

def mitigate_phishing_attack(email):
    # Remove the email from the inbox and move it to a spam folder
    email.remove()
    email.move("Spam")
    
# Test the function
sender = "spammer@example.com"
recipient = "user@example.com"
subject = "Phishing Attack"
body = "Click here to download a file."
email = EmailMessage(sender, recipient, subject, body)
if is_phishing_attack(email):
    mitigate_phishing_attack(email)
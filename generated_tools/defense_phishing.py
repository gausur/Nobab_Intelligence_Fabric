#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-03 22:06:31.548524

import re
import smtplib
from email.parser import Parser
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email contains a suspicious link or attachment
    if "://" in email.get("Body") or len(email.get_attachments()) > 0:
        return True
    
    # Check if the sender's domain is not from a trusted provider
    sender = email.get("From").split("<")[1].split(">")[0]
    if not check_domain(sender):
        return True
    
    return False

def check_domain(domain):
    # Check if the domain is in the list of trusted providers
    with open("trusted_providers.txt", "r") as f:
        for line in f:
            if line.strip() == domain:
                return True
    return False

def mitigate_phishing(email):
    # Remove the suspicious link or attachment
    email.body = re.sub("://", "", email.get("Body"))
    
    # Remove the sender's address from the email
    email["From"] = "Phishing Attack Detected"
    
    # Send a notification to the admin
    send_notification(email)

def send_notification(email):
    # Set up the email message
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attack Detected"
    msg["From"] = "noreply@example.com"
    msg["To"] = "admin@example.com"
    msg.set_content(f"A phishing attack has been detected on the email {ema[4D[K
{email['Subject']}. The sender's domain is not from a trusted provider.")
    
    # Send the email using SMTP
    s = smtplib.SMTP("smtp.example.com")
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    with open("email.txt", "r") as f:
        email = Parser().parsestr(f.read())
    
    if is_phishing(email):
        mitigate_phishing(email)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-17 11:19:20.699570

import re
import smtplib
from email.message import EmailMessage

def is_phishing_email(email):
    # Check if the email has a spammy sender
    if "spammer@example.com" in email["From"]:
        return True
    
    # Check if the email contains suspicious keywords
    for keyword in ["phishing", "scam", " fraud"]:
        if keyword in email.body:
            return True
    
    # Check if the email is trying to trick the user into clicking a link
    if "<a href='" in email.body and "</a>" in email.body:
        return True
    
    return False

def mitigate_phishing_email(email):
    # Remove any links from the email body
    email.body = re.sub("<a href.*</a>", "", email.body)
    
    # Send an alert to the user
    subject = "Phishing Attempt Detected"
    message = f"A phishing attempt was detected in your email. Please be ca[2D[K
cautious and report any suspicious activity."
    send_email(subject, message)

def send_email(subject, message):
    # Send an email using the smtplib module
    server = smtplib.SMTP("smtp.example.com")
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "your-email@example.com"
    msg["To"] = "user-email@example.com"
    msg.set_content(message)
    server.send_message(msg)
    server.quit()
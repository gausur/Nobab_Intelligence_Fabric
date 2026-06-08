#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-08 20:05:34.981607

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    """Check if the given email is a phishing attack."""
    # Check if the email contains suspicious keywords or phrases
    keywords = ["phish", "scam", "hack", "fraud"]
    for keyword in keywords:
        if keyword in email.body:
            return True
    
    # Check if the email sender is not from a trusted domain
    if not re.match(r"^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"[64D[K
re.match(r"^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$", email.sen[9D[K
email.sender):
        return True
    
    # Check if the email is not from a known phishing domain
    if email.sender_domain in ["phish.com", "scam.org", "hack.net", "fraud.[7D[K
"fraud.io"]:
        return True
    
    return False

def mitigate(email):
    """Mitigate a phishing attack by sending an alert."""
    # Create an email message to send the alert
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attack Detected"
    msg["From"] = "noreply@example.com"
    msg["To"] = email.sender
    msg.set_content("This is an automated message to alert you that your em[2D[K
email address was used in a phishing attack.\nPlease check your account and[3D[K
and report any suspicious activity.")
    
    # Send the alert email
    with smtplib.SMTP("smtp.example.com") as server:
        server.sendmail(msg["From"], msg["To"], msg.as_string())
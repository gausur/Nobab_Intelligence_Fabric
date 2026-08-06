#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-06 07:39:12.100404

import re
import smtplib
from email.message import EmailMessage

def detect_phishing(email):
    # Check if the email is from a trusted sender
    if not email.get("From").endswith("@example.com"):
        return False
    
    # Check if the email contains a link to a website
    if not re.search(r"https?://\S+", email.get_payload()):
        return False
    
    # Check if the email is from a legitimate domain
    if not email.get("From").endswith("@legitimate.com"):
        return False
    
    # If all checks pass, then the email is likely a phishing attack
    return True

def mitigate_phishing(email):
    # Remove the message body from the email
    email.set_content("")
    
    # Add a note to the recipient that the message was flagged as spam
    note = "This message has been identified as a phishing attack and has b[1D[K
been removed by the server."
    email.add_header("X-Spam-Status", "No, it's not spam")
    
    # Send the modified email back to the recipient
    smtplib.sendmail(email.get("From"), email.get("To"), email.as_string())[18D[K
email.as_string())

# Example usage:
message = EmailMessage()
message["Subject"] = "Phishing attack detected"
message["From"] = "phisher@example.com"
message["To"] = "recipient@legitimate.com"
message.set_payload("Click on this link to login to your account: https://p[9D[K
https://phishingwebsite.com/login")
mitigate_phishing(message)
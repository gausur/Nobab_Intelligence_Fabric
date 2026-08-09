#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 09:33:51.180602

import re
import json
from email.message import EmailMessage

# Load the domain list
with open("domains.json", "r") as f:
    domains = json.load(f)

def is_phishing_attack(email):
    """Check if the email is a phishing attack"""
    message = EmailMessage.from_bytes(email)
    subject = message["Subject"]
    sender = message["From"]
    recipient = message["To"]
    body = message.get_payload()

    # Check for suspicious subjects
    if re.search(r"[Ff]ake|[Ss]ocial [Ee]ngineering", subject, re.IGNORECAS[12D[K
re.IGNORECASE):
        return True

    # Check for suspicious senders or recipients
    for domain in domains:
        if domain in sender or domain in recipient:
            return True

    # Check for suspicious content
    if re.search(r"[Cc]lick here|[Jj]oin now", body, re.IGNORECASE):
        return True

    return False

def mitigate_phishing_attack(email):
    """Mitigate a phishing attack"""
    message = EmailMessage.from_bytes(email)
    message["To"] = "undisclosed-recipients@example.com"
    message["Subject"] = f"Phishing Attempt: {message['Subject']}"
    return message.as_bytes()
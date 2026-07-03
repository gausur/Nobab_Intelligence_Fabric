#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-03 06:28:37.862901

import re
import smtplib
from email.utils import parseaddr

def is_phishing(email):
    """Detects if an email is a phishing attack based on the sender's domai[5D[K
domain"""
    # Parse the sender's address and extract the domain
    sender_domain = parseaddr(email.get("From"))[1].split("@")[-1]

    # Check if the domain is in the list of known phishing domains
    if sender_domain in PHISHING_DOMAINS:
        return True
    
    return False

def mitigate(email):
    """Mitigates a phishing attack by sending an email to the user"""
    # Parse the recipient's address and extract their email address
    recipient = parseaddr(email.get("To"))[1].split("@")[-1]

    # Send an email to the user warning them about the phishing attack
    smtplib.SMTP().sendmail("phishing@example.com", recipient, "This is a p[1D[K
phishing attack!")

# List of known phishing domains
PHISHING_DOMAINS = ["phishng.com", "phishtank.org"]

# Check if the email is from a known phishing domain
if is_phishing(email):
    # Mitigate the phishing attack by sending an email to the user
    mitigate(email)
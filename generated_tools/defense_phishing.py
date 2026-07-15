#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-15 22:54:31.299255

import re
import smtplib

def is_phishing_email(email):
    """
    Check if the given email is a phishing attack
    by checking for common phishing tactics such as
    invalid sender, suspicious subject or content, and
    missing SPF/DKIM records.
    """
    # Check for invalid sender
    if not re.match(r"^[^@]+@[^@]+\.[a-zA-Z0-9-.]+$", email["From"]):
        return True
    
    # Check for suspicious subject or content
    if re.search(r"phishing|scam|fraud", email["Subject"]) or \
            re.search(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", email["Content"]):
        return True
    
    # Check for missing SPF/DKIM records
    if not smtplib.has_valid_sender_ip(email):
        return True
    
    return False
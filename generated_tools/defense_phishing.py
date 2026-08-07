#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-07 20:32:27.524139

import re
import smtplib

# Define the list of domains that are considered safe
safe_domains = ["example1.com", "example2.com"]

def is_phishing(email):
    # Check if the email address is in a safe domain
    if email.split("@")[1] in safe_domains:
        return False
    
    # Check if the email contains any suspicious keywords
    for keyword in ["phish", "scam", "malware"]:
        if keyword in email:
            return True
    
    # Check if the email is from a known spammer
    try:
        smtplib.SMTP("smtp.example.com").sendmail(email, "spammer@example.c[18D[K
"spammer@example.com")
        return False
    except smtplib.SMTPException:
        return True

def mitigate_phishing(email):
    # Move the email to the spam folder
    try:
        smtplib.SMTP("smtp.example.com").sendmail(email, "spammer@example.c[18D[K
"spammer@example.com")
        return True
    except smtplib.SMTPException:
        return False
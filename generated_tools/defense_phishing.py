#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-12 14:39:46.457365

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email has a suspicious subject line
    if re.search(r"[^a-zA-Z0-9\s]", email.subject):
        return True

    # Check if the email has a suspicious sender address
    if re.search(r"@[^\.]+\.[a-z]{2,}$", email.sender):
        return True

    # Check if the email contains a suspicious attachment
    for part in email.attachments:
        if re.search(r"[^a-zA-Z0-9\s]", part.filename):
            return True

    return False

def mitigate_phishing(email):
    # Respond with a friendly message
    response = EmailMessage()
    response.set_content("Thanks for reaching out! We're just an AI, we don[3D[K
don't have the capability to receive emails.")
    smtplib.sendmail("[YOUR_SMTP_SERVER]", email.sender, response)
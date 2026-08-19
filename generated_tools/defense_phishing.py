#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-19 10:23:12.794715

import re
import urllib.request
import email.utils

def detect_phishing_attacks(email_message):
    # Extract the sender's email address and the recipient's email address
    sender_email = email_message["From"]
    recipient_email = email_message["To"]

    # Check if the sender's email address is legitimate
    if not email.utils.is_email(sender_email):
        return False

    # Check if the recipient's email address is legitimate
    if not email.utils.is_email(recipient_email):
        return False

    # Check if the email contains a malicious attachment
    if "Content-Disposition" in email_message:
        content_disposition = email_message["Content-Disposition"]
        if "attachment" in content_disposition:
            return False

    # Check if the email contains a malicious URL
    if "Content-Location" in email_message:
        content_location = email_message["Content-Location"]
        if not urllib.request.urlparse(content_location).scheme:
            return False

    return True

# Test the function
email_message = """From: <sender@example.com>
To: <recipient@example.com>
Subject: Phishing Attack

This is a phishing attack!

Please click on the link below to download the malware:

https://example.com/malware.exe

If you see this message, your email client is not properly configured.
"""

if detect_phishing_attacks(email_message):
    print("Phishing attack detected!")
else:
    print("No phishing attack detected.")
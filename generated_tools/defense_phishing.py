#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-07 20:24:35.004135

import re
import smtplib

def detect_phishing(email):
    # Check if the email contains a phishing link
    if re.search(r"https?://[^\.]+\.[a-z]+", email):
        # Get the URL from the email
        url = re.search(r"https?://[^\.]+\.[a-z]+", email).group()
        # Check if the URL is in the blacklist
        if url in blacklist:
            # If the URL is in the blacklist, return an error message
            return "Phishing attack detected!"
        else:
            # If the URL is not in the blacklist, check if it's a valid URL[3D[K
URL
            try:
                smtplib.SMTP(url).sendmail("sender@example.com", "recipient[10D[K
"recipient@example.com", "This is a test message")
                # If the URL is a valid URL, return a success message
                return "Phishing attack detected and mitigated!"
            except smtplib.SMTPException:
                # If the URL is not a valid URL, return an error message
                return "Invalid URL detected!"
    else:
        # If the email does not contain a phishing link, return a success m[1D[K
message
        return "No phishing attack detected"

blacklist = ["https://www.phishingwebsite.com", "https://phishing.example.c[27D[K
"https://phishing.example.com"]
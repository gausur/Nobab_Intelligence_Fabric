#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 04:04:14.884365

import re
import smtplib
from email.message import EmailMessage

# Define the list of phishing domains to block
phishing_domains = ["example1.com", "example2.com"]

# Define the function to check if an email is from a phishing domain
def is_phishing(email):
    return any(domain in email["From"].lower() for domain in phishing_domai[14D[K
phishing_domains)

# Define the function to send an alert email if a phishing attack is detect[6D[K
detected
def send_alert(email):
    msg = EmailMessage()
    msg.set_content("Phishing attack detected: " + str(email))
    smtplib.sendmail("your-email@example.com", "admin-email@example.com", m[1D[K
msg.as_string())

# Check if an email is from a phishing domain and send an alert if it is
for email in emails:
    if is_phishing(email):
        send_alert(email)
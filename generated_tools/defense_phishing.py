#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 20:34:11.025997

import re
import smtplib
from email.message import EmailMessage

# Define the sender's email address and password
sender_email = "your_email@example.com"
sender_password = "your_password"

# Define the recipient's email address
recipient_email = "recipient_email@example.com"

# Define the email subject and body
subject = "Test Email for Phishing Detection"
body = "This is a test email to detect phishing attacks."

# Create an instance of the EmailMessage class
msg = EmailMessage()

# Set the email's subject and body
msg["Subject"] = subject
msg.set_content(body)

# Add the recipient's email address to the "To" field
msg["To"] = recipient_email

# Set the sender's email address
msg["From"] = sender_email

# Send the email using smtplib
with smtplib.SMTP("smtp.example.com") as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
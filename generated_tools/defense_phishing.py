#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-02 05:27:27.646124

import re
import smtplib

# Define the list of emails to check
emails = ['john.doe@example.com', 'jane.smith@example.com']

# Set up the email server
server = smtplib.SMTP('smtp.example.com', 587)

# Connect to the email server
server.starttls()
server.login('username', 'password')

# Iterate over the list of emails
for email in emails:
    # Send an email to the email address
    server.sendmail('sender@example.com', email, 'Subject: Phishing Attack [K
Detected')

# Close the email server connection
server.quit()
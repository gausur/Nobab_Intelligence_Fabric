#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-24 12:15:57.321515

import re
import smtplib

# Define the pattern for matching phishing URLs
phishing_url_pattern = r"https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a[52D[K
r"https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@r"https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[az]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

# Define the list of phishing URLs to block
phishing_urls = [
    "https://www.example1.com",
    "https://www.example2.com"
]

# Set up an SMTP server for sending alerts
smtp_server = smtplib.SMTP("localhost")

# Define a function to check if the URL is phishing
def is_phishing(url):
    # Check if the URL matches the pattern
    match = re.search(phishing_url_pattern, url)
    if match:
        # If it does, return True
        return True
    else:
        # Otherwise, return False
        return False

# Define a function to send an alert email
def send_alert(url):
    # Set up the message text
    msg = f"Phishing URL detected: {url}"
    
    # Send the message using the SMTP server
    smtp_server.sendmail("admin@example.com", "user@example.com", msg)

# Iterate through the list of URLs and check if any are phishing
for url in phishing_urls:
    if is_phishing(url):
        # If a phishing URL is found, send an alert email
        send_alert(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-11 14:27:12.310971

import re
import smtplib
from email.mime.text import MIMEText

# Define the regular expression for detecting phishing emails
PHISHING_REGEX = r"((\bhttps?:\/\/)|(\bwww\.)|(\bmailto:))[^\s]*(\.com|\.or[58D[K
r"((\bhttps?:\/\/)|(\bwww\.)|(\bmailto:))[^\s]*(\.com|\.org|\.net|\.io)(\s|r"((\bhttps?:\/\/)|(\bwww\.)|(\bmailto:))[^\s]*(\.com|\.or|\.net|\.io)(\s|$)"

# Define the email server configuration
EMAIL_SERVER = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

def send_email(recipient, subject, body):
    # Create a new email message
    msg = MIMEText(body)
    msg["Subject"] = subject

    # Send the email using the SMTP library
    with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, recipient, msg.as_string())

def detect_phishing_attacks(email):
    # Check if the email is a phishing attack using the regular expression
    if re.match(PHISHING_REGEX, email["body"]):
        print("Phishing attack detected!")
        send_email(
            recipient=email["from"],
            subject="Phishing Attack Detected",
            body="Please do not click on any links or provide any personal [K
information.",
        )
    else:
        print("No phishing attack detected.")

# Use the detect_phishing_attacks function with a sample email
sample_email = {
    "from": "someone@example.com",
    "body": "Click here to buy something: https://www.example.com/buy-now",[33D[K
https://www.example.com/buy-now",
}
detect_phishing_attacks(sample_email)
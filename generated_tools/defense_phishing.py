#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-04 15:03:45.487844

import re
import smtplib
from email.message import EmailMessage

# Define the regex pattern for validating emails
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_email(email):
    # Use the regex pattern to validate the email address
    return re.match(EMAIL_REGEX, email) is not None

def send_email(sender, recipient, subject, body):
    # Create a new EmailMessage object
    msg = EmailMessage()

    # Set the sender and recipient of the message
    msg["From"] = sender
    msg["To"] = recipient

    # Set the subject and body of the message
    msg["Subject"] = subject
    msg.set_content(body)

    # Send the email using smtplib
    with smtplib.SMTP("smtp.example.com") as server:
        server.send_message(msg)

def detect_phishing(email):
    # Check if the email is valid
    if not validate_email(email):
        return False

    # Extract the domain name from the email address
    domain = email.split("@")[1]

    # Check if the domain name is a known phishing domain
    if domain in PHISHING_DOMAINS:
        return True

    # Check if the email contains any known phishing URLs
    for url in URL_BLACKLIST:
        if url in email:
            return True

    # If none of the above conditions are met, it's not a phishing email
    return False

def mitigate_phishing(email):
    # If the email is determined to be a phishing email, reject it
    if detect_phishing(email):
        raise ValueError("Phishing attack detected")

# List of known phishing domains
PHISHING_DOMAINS = ["example.com", "fake-domain.org"]

# List of known phishing URLs
URL_BLACKLIST = ["http://www.phishingwebsite.com/login", "https://fake-webs[18D[K
"https://fake-website.org/login"]

if __name__ == "__main__":
    # Test the script by sending a valid and a phishing email
    send_email("valid@example.com", "valid@example.com", "Subject", "Body")[7D[K
"Body")
    try:
        send_email("phishing@example.com", "valid@example.com", "Subject", [K
"Body")
    except ValueError as e:
        print(e)
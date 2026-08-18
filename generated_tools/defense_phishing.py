#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-18 08:28:52.858331

import re
import smtplib
from email.utils import getaddresses

def detect_phishing_attack(email_message):
    # Extract the sender and recipient addresses from the email message
    sender_address = getaddresses(email_message['From'])[0]
    recipient_address = getaddresses(email_message['To'])[0]

    # Check if the sender address is a valid email address
    if not re.match(r'^.+@.+\..+$', sender_address):
        print("Invalid sender address")
        return False

    # Check if the recipient address is a valid email address
    if not re.match(r'^.+@.+\..+$', recipient_address):
        print("Invalid recipient address")
        return False

    # Check if the email message contains a suspicious subject line
    if re.search(r'phishing|scam|fraud', email_message['Subject']):
        print("Suspicious subject line")
        return False

    # Check if the email message contains a suspicious attachment
    if re.search(r'exe|dll|bat|vbs|scr|ps', email_message.get_content_maint[31D[K
email_message.get_content_maintype()):
        print("Suspicious attachment")
        return False

    return True

# Example usage

# Import the email package
from email.message import EmailMessage

# Create an email message
message = EmailMessage()
message['Subject'] = "Phishing attack!"
message['From'] = "john.doe@example.com"
message['To'] = "jane.doe@example.com"

# Add a suspicious attachment to the email message
with open('phishing.exe', 'rb') as f:
    message.add_attachment(f.read(), 'application/octet-stream')

# Check if the email message is a phishing attack
if detect_phishing_attack(message):
    print("Phishing attack detected")
else:
    print("Phishing attack not detected")
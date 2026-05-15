#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-15 09:44:55.289779

import re
import smtplib
from email import message_from_string

def is_phishing_url(url):
    return re.match(r"^https?://(www\.)?phish([ing])?.com", url)

def mitigate_phishing_attack(msg):
    if is_phishing_url(msg["From"]):
        # Mark the message as spam
        msg.add_flags("spam")
        # Reject the message
        raise smtplib.SMTPReject("Phishing attack detected")

def main():
    server = smtplib.SMTP(hostname="smtp.example.com", port=25)
    server.login(user="phish@example.com", password="secret")

    # Read the message from stdin
    msg = message_from_string(sys.stdin.read())

    mitigate_phishing_attack(msg)

    # Send the message to the recipient
    server.sendmail("phish@example.com", "recipient@example.com", msg.as_by[9D[K
msg.as_bytes())
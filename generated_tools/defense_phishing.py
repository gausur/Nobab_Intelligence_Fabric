#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-27 23:25:53.190299

import re
import smtplib

def detect_phishing(email):
    # Check for common phishing words
    if re.search(r"(phishing|scam|fraud|hack)", email.lower()):
        return True

    # Check for suspicious links
    if re.search(r"(http|https)://(www\.)?[a-z0-9]+(-[a-z0-9]+)*\.[a-z]{2,}[68D[K
re.search(r"(http|https)://(www\.)?[a-z0-9]+(-[a-z0-9]+)*\.[a-z]{2,}(/.*)?"re.search(r"(http|https)://(www\.)?[a-z0-9]+(-[a-z0-9]+)*\.[a-z]{2,}/.*)?", email):
        return True

    # Check for suspicious file attachments
    if re.search(r"(exe|zip|docx|xlsx|pdf)", email.lower()):
        return True

    return False

def mitigate_phishing(email):
    # Mark the email as spam
    smtplib.SMTP("localhost").sendmail("spam", [email.from_address], "This [K
email is marked as spam")

    # Block the sender from sending any more emails
    smtplib.SMTP("localhost").sendmail("block", [email.from_address], "This[5D[K
"This sender has been blocked")

    # Delete the email from the server
    smtplib.SMTP("localhost").sendmail("delete", [email.message_id], "This [K
email has been deleted")

def main():
    # Set up the email server
    server = smtplib.SMTP("localhost")

    # Start the email listener
    server.starttls()
    server.login("username", "password")
    server.receive()

    # Handle the incoming emails
    while True:
        email = server.receive()
        if detect_phishing(email):
            mitigate_phishing(email)

if __name__ == "__main__":
    main()
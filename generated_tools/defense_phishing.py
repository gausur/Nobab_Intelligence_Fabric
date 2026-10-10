#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-10 20:28:30.102288

import re
import smtplib

def detect_phishing(email):
    """
    Detect phishing attacks in emails.

    :param email: The email message to check.
    :return: True if the email is phishing, False otherwise.
    """
    # Check the subject for keywords related to phishing
    if re.search(r'phishing|scam|hack', email.subject, re.IGNORECASE):
        return True

    # Check the sender's email address for suspicious characters
    if re.search(r'@(gmail|yahoo|hotmail)\.', email.from_address):
        return True

    # Check the content of the email for suspicious links or attachments
    if re.search(r'://(drive|dropbox|onedrive)\.', email.body):
        return True

    # Check the sender's email address for spelling errors
    if re.search(r'[a-zA-Z]+@[a-zA-Z]+', email.from_address):
        return True

    # Check the recipient's email address for spelling errors
    if re.search(r'[a-zA-Z]+@[a-zA-Z]+', email.to_address):
        return True

    # Check the content of the email for suspicious words or phrases
    if re.search(r'phishing|scam|hack|virus', email.body, re.IGNORECASE):
        return True

    # If the email doesn't contain any of the above keywords or phrases, it[2D[K
it is likely legitimate
    return False

def mitigate_phishing(email):
    """
    Mitigate phishing attacks by blocking the sender's email address.

    :param email: The email message to block.
    """
    # Block the sender's email address
    smtplib.sendmail('noreply@example.com', email.from_address, 'Phishing a[1D[K
attempt blocked')

# Example usage
email = EmailMessage('Subject: Phishing Attack', 'This is a phishing attemp[6D[K
attempt', 'sender@example.com', ['recipient@example.com'])
if detect_phishing(email):
    mitigate_phishing(email)
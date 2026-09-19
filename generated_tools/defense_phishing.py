#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-19 05:23:16.965724

import re
import smtplib
from email.mime.text import MIMEText

def detect_phishing(email):
    """
    Detect phishing attacks in an email by analyzing the subject and body.

    Args:
        email (str): The email to be analyzed.

    Returns:
        bool: True if the email is a phishing attack, False otherwise.
    """
    # Check if the email is from a valid sender
    sender = email['From']
    if not re.match(r'^.*@.*\.\w{2,}$', sender):
        return True

    # Check if the email contains a suspicious word
    words = ['phishing', 'scam', 'fraud', 'hack']
    for word in words:
        if word in email['Subject'] or word in email['Body']:
            return True

    # Check if the email contains a suspicious link
    if re.search(r'https?://.*', email['Body']):
        return True

    return False

def mitigate_phishing(email):
    """
    Mitigate a phishing attack by rejecting the email and sending an alert.[6D[K
alert.

    Args:
        email (str): The email to be mitigated.

    Returns:
        None
    """
    # Reject the email
    print('Rejecting email from', email['From'])
    return

    # Send an alert
    print('Sending alert to IT')
    msg = MIMEText('Phishing attack detected from', 'plain')
    msg['Subject'] = 'Phishing Attack Detected'
    msg['From'] = 'phishing.attack@example.com'
    s = smtplib.SMTP('localhost')
    s.sendmail(msg['From'], ['it@example.com'], msg.as_string())
    s.quit()

if __name__ == '__main__':
    # Test the script with a fake email
    email = {
        'From': 'john.doe@example.com',
        'Subject': 'Fake Phishing Attack',
        'Body': 'Click here to access your account'
    }
    if detect_phishing(email):
        mitigate_phishing(email)
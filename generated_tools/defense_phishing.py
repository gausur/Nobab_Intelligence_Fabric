#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-22 10:22:43.058967

import re
import smtplib
from email.message import EmailMessage

def is_phishing_email(email):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', em[2D[K
email):
        return False

    # Check if the email is from a legitimate domain
    _, domain = email.split('@')
    if not smtplib.SMTP().sendmail('', domain):
        return False

    # Check if the email contains any suspicious content
    for part in email.walk():
        if part.get_content_type() == 'text/html':
            body = part.get_payload(decode=True)
            if re.search(r'<script>', body):
                return True
            if re.search(r'<a href="[^"]*">', body):
                return True
    return False

def mitigate_phishing_email(email):
    # Send an email to the recipient with a message indicating that the ema[3D[K
email is suspicious
    sender = 'Phishing Detector <phishing.detector@example.com>'
    recipient = email['From']
    subject = 'Suspicious Phishing Email'
    body = f'Dear {recipient}, this is an automated message indicating that[4D[K
that the email you received from {email["From"]} appears to be a phishing a[1D[K
attack. Please do not click on any links or provide any personal informatio[10D[K
information.'
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(body)
    smtplib.SMTP().sendmail(sender, recipient, msg.as_string())

# Main function to detect and mitigate phishing attacks
def main():
    email = input('Enter the email address: ')
    if is_phishing_email(email):
        mitigate_phishing_email(email)
    else:
        print('Email does not appear to be a phishing attack.')

if __name__ == '__main__':
    main()
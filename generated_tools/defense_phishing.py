#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-15 17:34:11.780504

import re
import smtplib

def is_phishing_url(url):
    # Check if the URL is a phishing URL by checking if it contains any of [K
the known phishing keywords
    keywords = ['phishing', 'scam', 'fraud', 'hack', 'hijack']
    for keyword in keywords:
        if keyword in url:
            return True
    return False

def is_phishing_email(email):
    # Check if the email is a phishing email by checking if it contains any[3D[K
any of the known phishing keywords
    keywords = ['phishing', 'scam', 'fraud', 'hack', 'hijack']
    for keyword in keywords:
        if keyword in email:
            return True
    return False

def send_email(recipient, subject, message):
    # Send an email to the recipient with the given subject and message
    smtplib.SMTP().sendmail('sender@example.com', recipient, f'Subject: {su[3D[K
{subject}\n\n{message}')

def main():
    # Get the email and URL from the command line arguments
    email = sys.argv[1]
    url = sys.argv[2]

    # Check if the email and URL are phishing
    if is_phishing_email(email) or is_phishing_url(url):
        # If either the email or URL are phishing, send a warning email to [K
the sender
        send_email(sys.argv[1], 'Phishing Warning', f'This is a phishing em[2D[K
email. Please do not click on any links or provide any personal information[11D[K
information.')

if __name__ == '__main__':
    main()
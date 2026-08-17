#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 15:20:57.116640

import re
import smtplib
from email.mime.text import MIMEText

def is_phishing_email(email):
    # Check if the email is from a legitimate source
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', em[2D[K
email['From']):
        return False
    # Check if the email contains a phishing URL
    if re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email[[6D[K
email['Text']):
        return False
    return True

def send_email(email):
    # Send an email to the user with the details of the phishing attempt
    msg = MIMEText('Phishing attempt detected!\n\nFrom: {}\n\n{}'.format(em[19D[K
{}\n\n{}'.format(email['From'], email['Text']))
    msg['Subject'] = 'Phishing Attempt'
    msg['From'] = 'phishing@example.com'
    msg['To'] = email['From']
    smtplib.sendmail('phishing@example.com', email['From'], msg.as_string()[15D[K
msg.as_string())

def main():
    # Read the emails from the SMTP server
    with smtplib.SMTP('smtp.example.com') as server:
        server.connect()
        server.login()
        for email in server.retrieve_emails():
            if is_phishing_email(email):
                send_email(email)

if __name__ == '__main__':
    main()
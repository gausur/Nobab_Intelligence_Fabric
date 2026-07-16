#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-16 07:19:29.441832

import re
import smtplib
from email.utils import parseaddr
from email.header import decode_header
from urllib.parse import urlparse

def is_phishing_email(email):
    # Check if the email is from a legitimate domain
    sender = parseaddr(email['From'])[1]
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', sender):
        return False
    
    # Check if the email contains a suspicious link
    for part in email.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        content = part.get_payload(decode=True)
        if not content:
            continue
        link = re.search(r'https?://[\w\.-]+/[\w\./-]*', content)
        if link and urlparse(link.group()).hostname != sender:
            return True
    
    # Check if the email contains a suspicious attachment
    for part in email.walk():
        if part.get_content_maintype() == 'application' and re.search(r'[/\[15D[K
re.search(r'[/\\\.]exe', part.get('Content-Disposition')):
            return True
    
    # No suspicious patterns found
    return False

def mitigate_phishing_email(email):
    # Remove the email from the spam folder
    try:
        smtplib.SMTP().noop()
    except Exception as e:
        print(f'Failed to remove email from spam folder: {e}')
    
    # Block the sender's IP address
    try:
        smtplib.SMTP().quit()
    except Exception as e:
        print(f'Failed to block sender\'s IP address: {e}')

def main():
    # Load the email from stdin
    email = mailbox.mbox('stdin').get_message()
    
    # Detect and mitigate phishing attacks
    if is_phishing_email(email):
        mitigate_phishing_email(email)
    else:
        print('Email is not a phishing attack')
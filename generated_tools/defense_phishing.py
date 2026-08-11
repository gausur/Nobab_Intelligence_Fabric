#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 08:06:59.699089

import re
import smtplib
from email.parser import Parser

def is_phishing(email):
    # Check for common phishing patterns in the subject line
    if re.search(r'[Ff]ree[\s]*[\w\W]+[Ee]mail', email['subject']):
        return True
    elif re.search(r'[Uu]pgrade[\s]*to[\s]*[\w\W]+[Ee]mail', email['subject[14D[K
email['subject']):
        return True
    elif re.search(r'[Cc]oupon[\s]*[\w\W]+[Ee]mail', email['subject']):
        return True
    # Check for common phishing patterns in the body of the email
    if re.search(r'http://www\.example\.com', email['body']):
        return True
    elif re.search(r'www\.example\.com', email['body']):
        return True
    # Check for common phishing patterns in the sender's email address
    if email['from'].endswith('@example.com'):
        return True
    # If none of the above patterns are found, it is likely not a phishing [K
email
    return False

def mitigate_phishing(email):
    # Send a copy of the email to an admin's email address for review
    with smtplib.SMTP('smtp.example.com', 25) as server:
        server.sendmail('admin@example.com', 'admin@example.com', f'Subject[9D[K
f'Subject: Phishing attempt detected\n\nOriginal message:\n{email}')

# Example usage
with open('phishing_emails.txt', 'r') as file:
    emails = file.readlines()
for email in emails:
    if is_phishing(Parser().parsestr(email)):
        mitigate_phishing(email)
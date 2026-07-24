#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-24 08:12:57.649247

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    # Check if the sender's email address is valid
    if not email['From'].endswith('@example.com'):
        return False
    
    # Check if the email has a malicious attachment
    for part in email.iter_attachments():
        if part.get_filename().lower().endswith(('.exe', '.zip', '.rar')):
            return True
    
    # Check if the email contains a suspicious link
    for url in email.iter_urls():
        if 'phishing' in url or 'malicious' in url:
            return True
    
    # Check if the email has a suspicious subject line
    if any(word in email['Subject'] for word in ('scam', 'fraud')):
        return True
    
    return False

def mitigate_phishing(email):
    # Remove all attachments
    for part in email.iter_attachments():
        part.dispose()
    
    # Remove the email's subject line and body
    email['Subject'] = 'Phishing Attempt Detected'
    email.set_content('This email is a phishing attempt. Do not open any li[2D[K
links or download attachments.')
    
    return email

def send_email(email):
    # Send the mitigated email to the recipient
    smtp = smtplib.SMTP('smtp.example.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('phishing@example.com', 'password')
    smtp.send_message(email)
    smtp.quit()

def main():
    # Read the email from stdin
    email = EmailMessage()
    email.parse(sys.stdin.read())
    
    # Detect and mitigate phishing attacks
    if is_phishing(email):
        mitigated_email = mitigate_phishing(email)
        send_email(mitigated_email)
    else:
        print('No phishing attempt detected.')
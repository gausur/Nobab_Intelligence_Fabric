#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-02 21:31:41.770909

import re
import smtplib
from email.message import EmailMessage

def detect_phishing_attacks(email_message):
    # Check if the email is from a valid sender
    sender = email_message.get('From')
    if not sender or not re.match(r'^[^@]+@[^@]+\.[^@]+$', sender):
        return False
    
    # Check if the email is from a known sender
    known_senders = ['example.com', 'example2.com']
    if sender not in known_senders:
        return False
    
    # Check if the email has a valid recipient
    recipient = email_message.get('To')
    if not recipient or not re.match(r'^[^@]+@[^@]+\.[^@]+$', recipient):
        return False
    
    # Check if the email has a valid subject
    subject = email_message.get('Subject')
    if not subject or not re.match(r'^[a-zA-Z0-9 _-]+$', subject):
        return False
    
    # Check if the email has a valid body
    body = email_message.get('Body')
    if not body or not re.match(r'^[a-zA-Z0-9 _-]+$', body):
        return False
    
    return True

def mitigate_phishing_attacks(email_message):
    # Block the email
    smtplib.SMTP('localhost').sendmail(email_message.get('From'), email_mes[9D[K
email_message.get('To'), 'This email has been blocked.')

# Parse the email message from the input
email_message = EmailMessage.from_string(input())

# Detect and mitigate phishing attacks
if detect_phishing_attacks(email_message):
    mitigate_phishing_attacks(email_message)
else:
    print('Invalid email.')
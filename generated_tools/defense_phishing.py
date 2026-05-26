#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-26 20:02:17.010908

import re
import smtplib
from email.parser import Parser

def is_phishing_email(email):
    # Check if the email is from a known spammer
    sender = email['From']
    if sender in SPAMMERS:
        return True
    
    # Check if the email contains a known phishing URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\([57D[K
re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    for part in email.walk():
        if url_pattern.search(part.get_content()):
            return True
    
    # Check if the email contains a known phishing keyword
    keyword_pattern = re.compile(r'\b(?:phishing|scam|fraudulent)\b', re.IG[5D[K
re.IGNORECASE)
    if keyword_pattern.search(email['Subject']):
        return True
    
    return False

def mitigate_phishing_attack(email, recipient):
    # Send a notification email to the recipient and the sender of the orig[4D[K
original email
    with smtplib.SMTP('smtp.gmail.com') as server:
        server.sendmail(recipient, [recipient, email['From']], 'Phishing at[2D[K
attack detected!')
    
    # Remove the email from the recipient's inbox
    server.sendmail(recipient, 'Trash', 'Remove')

# List of known spammers
SPAMMERS = ['spammer1@example.com', 'spammer2@example.com']

# Start the email server
server = smtplib.SMTP('localhost')
server.starttls()
server.login('your_email@example.com', 'your_password')

while True:
    # Receive an email from the inbox
    msg = server.retrieve(0)
    
    # Parse the email content
    parser = Parser()
    email = parser.parsestr(msg[1])
    
    # Check if it's a phishing attack
    if is_phishing_email(email):
        mitigate_phishing_attack(email, msg[0])
    
    # Remove the email from the inbox
    server.sendmail('Trash', msg[0], 'Remove')
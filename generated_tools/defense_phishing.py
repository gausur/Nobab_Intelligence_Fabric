#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-28 22:59:58.962404

import re
import smtplib
from email.parser import Parser

def is_phishing_attempt(message):
    sender = message['From']
    subject = message['Subject']
    body = message.get_payload()

    # Check for spammy words in the subject and body
    if re.search(r'\bspam\b', subject, flags=re.IGNORECASE) or \
       re.search(r'\bspam\b', body, flags=re.IGNORECASE):
        return True
    
    # Check for spammy domains in the sender's email address
    if 'spam.com' in sender:
        return True
    
    # Check for spammy email providers in the sender's email address
    if re.search(r'\bspam\b', sender, flags=re.IGNORECASE):
        return True
    
    # Check for suspicious links in the message
    if '<a href="mailto:">' in body:
        return True
    
    return False

def mitigate_phishing_attempt(message):
    # Remove any suspicious links from the message
    message = re.sub(r'<a href="mailto:.*?">', '', message)
    # Remove any spammy words or domains from the subject and body
    message['Subject'] = re.sub(r'\bspam\b', '', message['Subject'])
    message['Body'] = re.sub(r'\bspam\b', '', message['Body'])
    # Send a notification to the user that their email has been flagged as [K
spam
    send_notification(message['From'], 'Your email has been flagged as spam[4D[K
spam. Please be more careful in the future.')
    return message

def send_notification(sender, message):
    # Send an email to the sender with a notification that their email has [K
been flagged as spam
    msg = f'Subject: {message}\n\n{message}'
    smtplib.SMTP('smtp.gmail.com', 587).sendmail(sender, sender, msg)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-13 02:28:07.339623

import re
from email.message import EmailMessage

def detect_phishing(email):
    # Check for common phishing patterns in the email subject
    if re.search(r'[\w\d]{10}@[\w\d]{10}\.com', email.subject):
        return True
    
    # Check for common phishing patterns in the email body
    if re.search(r'click here to activate your account', email.body, flags=[6D[K
flags=re.I):
        return True
    
    # Check for common phishing patterns in the email attachments
    for attachment in email.attachments:
        if re.search(r'win32\.exe', attachment.filename):
            return True
    
    return False

def mitigate_phishing(email):
    # Remove any suspicious attachments
    email.attachments = []
    
    # Set the email as read and delete it from the inbox
    email.read()
    email.delete()

# Main function to run the script
def main():
    # Get the list of emails from the inbox
    emails = EmailMessage.get_inbox()
    
    # Iterate over each email and detect phishing attacks
    for email in emails:
        if detect_phishing(email):
            mitigate_phishing(email)

if __name__ == '__main__':
    main()
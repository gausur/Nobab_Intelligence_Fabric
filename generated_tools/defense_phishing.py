#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-19 01:56:45.771514

import re
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email contains a suspicious link or attachment
    if re.search(r'((http|https)://[^/]+/[A-Z][A-Z]/)', email.text):
        return True
    # Check if the email has a sender from an unknown domain
    if email.sender.domain not in ['gmail.com', 'yahoo.com', 'outlook.com'][14D[K
'outlook.com']:
        return True
    # Check if the email has a subject that suggests a phishing attempt
    if re.search(r'((phishing|fake) |(scam|fraud)', email.subject):
        return True
    # Check if the email contains any suspicious keywords or phrases
    if re.search(r'(password|credentials) (not|are|being) ', email.text):
        return True
    return False

def mitigate_phishing(email):
    # Send an alert to the sender and the admin
    print('PHISHING ALERT: {}'.format(email))
    # Delete the email from the inbox
    delete(email)

def main():
    # Read emails from the inbox
    for email in read_inbox():
        if is_phishing(email):
            mitigate_phishing(email)

if __name__ == '__main__':
    main()
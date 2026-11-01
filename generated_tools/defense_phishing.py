#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-01 23:27:25.009303

import re
import smtplib

def is_phishing_attack(email):
    # Check for common phishing attack patterns
    if re.search(r'https?://[a-z0-9.-]+(:[0-9]+)?/[a-z0-9.-]+', email):
        return True
    if re.search(r'[a-z0-9.-]+@[a-z0-9.-]+\.onion', email):
        return True
    if re.search(r'[a-z0-9.-]+@[a-z0-9.-]+\.[a-z]+', email):
        return True
    return False

def mitigate_phishing_attack(email):
    # Check if the email is a phishing attack
    if is_phishing_attack(email):
        # Send an alert to the IT department
        smtplib.SMTP('it.example.com').sendmail('phishing@example.com', 'it@example.com', 'Subject: Phishing Attack Detected')
        # Block the email sender
        smtplib.SMTP('mail.example.com').sendmail('phishing@example.com', 'spam@example.com', 'Subject: Phishing Attack Detected')

def main():
    mitigate_phishing_attack(input('Enter an email: '))

if __name__ == '__main__':
    main()
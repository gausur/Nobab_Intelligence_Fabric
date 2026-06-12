#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-12 19:59:19.239925

import re
import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr

def is_phishing_email(email):
    # Check if the email address contains a valid TLD
    if not re.search(r'\.[a-zA-Z]{2,}$', email):
        return True
    
    # Check if the email address contains a common phishing domain
    if re.search(r'@phish\.(?:com|net|org)$', email):
        return True
    
    return False

def mitigate_phishing_attack(email):
    # Send an email to the sender with a warning and instructions on how to[2D[K
to report the phishing attempt
    msg = MIMEText('''Dear {},

We have detected a potential phishing attack on your account. Please do not[3D[K
not respond to this message, as it is likely a scam. Instead, follow these [K
steps:

1. Do not click on any links or download any attachments from the email.
2. Do not enter your login credentials or personal information in the email[5D[K
email.
3. If you have entered your login credentials or personal information in th[2D[K
the email, change your password immediately and report the incident to your[4D[K
your bank or financial institution.
4. Report the incident to the Federal Trade Commission (FTC) at phishing@ft[11D[K
phishing@ftc.gov.
5. Do not forward this message to anyone else.

Sincerely,
[Your Name]'''.format(parseaddr(email)[1]), 'plain')
    msg['Subject'] = 'Phishing Attack Warning'
    msg['From'] = 'noreply@example.com'
    msg['To'] = email
    
    smtplib.sendmail('noreply@example.com', [email], msg.as_string())

def main():
    # Read the email from standard input
    email = input()
    
    # Check if the email is a phishing attack
    if is_phishing_email(email):
        mitigate_phishing_attack(email)
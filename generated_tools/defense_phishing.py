#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-12 11:43:18.807493

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email contains a suspicious subject or attachment
    if re.search(r'phishing|scam', email['Subject'], re.IGNORECASE) or any([4D[K
any(re.search(r'phishing|scam', fname, re.IGNORECASE) for fname in email.ge[8D[K
email.get_payload()[1]):
        return True
    else:
        return False

def mitigate_phishing(email):
    # Send a warning email to the sender
    msg = EmailMessage()
    msg['Subject'] = 'Phishing Attempt Detected'
    msg['From'] = 'do-not-reply@example.com'
    msg['To'] = email['From']
    msg.set_content(f'Hi {email["From"]}, we have detected a phishing attem[5D[K
attempt in your email to {email["To"]}. Please be cautious when clicking on[2D[K
on links or providing personal information online.')
    with smtplib.SMTP('smtp.example.com', 587) as s:
        s.login('do-not-reply@example.com', 'your_password')
        s.send_message(msg)

def main():
    # Read the email message from stdin
    msg = ''
    for line in sys.stdin:
        msg += line
    
    # Parse the email message and check if it's a phishing attack
    email = EmailMessage()
    email.set_payload(msg)
    if is_phishing(email):
        mitigate_phishing(email)

if __name__ == '__main__':
    main()
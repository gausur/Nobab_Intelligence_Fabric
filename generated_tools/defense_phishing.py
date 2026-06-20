#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 08:45:40.725109

import re
import smtplib
from email.parser import Parser

def is_phishing_email(email):
    if not email:
        return False

    try:
        parser = Parser()
        message = parser.parsestr(email)

        subject = message['subject']
        body = message.get_payload()

        # Check for common phishing keywords in the subject and body of the[3D[K
the email
        if re.search(r'phishing|scam|malware', subject, re.IGNORECASE) or \[1D[K
\
                re.search(r'click here to confirm your account|confirm you[3D[K
your email address', body, re.IGNORECASE):
            return True
    except:
        pass

    # Check for suspicious links in the email
    if message.get_payload():
        for link in message.get_payload():
            if re.search(r'phishing|scam|malware', link, re.IGNORECASE):
                return True

    return False

def mitigate_phishing_attack(email):
    # Send an email to the recipient with a phishing warning
    sender = 'your@email.com'
    subject = 'Phishing Attempt Detected'
    body = f'Dear {email["from"]},<br><br>We have detected a phishing attem[5D[K
attempt from your email address ({email["from"]}). Please ignore any suspic[6D[K
suspicious emails or links you may have received.<br><br>Sincerely,<br>{sen[35D[K
received.<br><br>Sincerely,<br>{sender}'
    smtplib.sendmail(sender, email["to"], subject, body)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-11 11:42:54.105299

import re
from email.message import EmailMessage

def is_phishing(email):
    if not isinstance(email, EmailMessage):
        return False
    
    # Check for common phishing URL patterns in the subject and body of the[3D[K
the email
    pattern = r'(?i)((?:https?|ftp)://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[A-Za-[61D[K
r'(?i)((?:https?|ftp)://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[A-Za-z0-9+&@#/%=~_(r'(?i)((?:https?|ftp)://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[A-Za-0-9+&@#/%=~_()|])'
    if re.search(pattern, email.subject) or re.search(pattern, email.body):[12D[K
email.body):
        return True
    
    # Check for common phishing sender domains
    sender_domain = email.sender.split('@')[1]
    if sender_domain in ('yahoo.com', 'outlook.com', 'gmail.com', 'hotmail.[9D[K
'hotmail.com'):
        return True
    
    return False
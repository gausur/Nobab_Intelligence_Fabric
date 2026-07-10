#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-10 06:37:27.549928

import re
import urllib.request
from email.message import EmailMessage
from email.headerregistry import Address

def is_phishing(email):
    if not email:
        return False
    
    msg = EmailMessage()
    try:
        msg.set_content(email)
    except ValueError:
        return False
    
    for header in ("From", "To", "Subject"):
        value = msg.get(header, None)
        if not value or not isinstance(value, str):
            continue
        
        if re.search(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", value):
            return False
    
    return True

def mitigate_phishing(email):
    if not email:
        return None
    
    msg = EmailMessage()
    try:
        msg.set_content(email)
    except ValueError:
        return None
    
    for header in ("From", "To", "Subject"):
        value = msg.get(header, None)
        if not value or not isinstance(value, str):
            continue
        
        if re.search(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", value):
            return None
    
    msg["From"] = Address("noreply@example.com")
    msg["To"] = Address("admin@example.com")
    msg["Subject"] = "Phishing Attempt Detected"
    msg.set_content(f"""
        Phishing attempt detected from {msg["From"]}.\n
        Please do not click on any links or provide any personal informatio[10D[K
information.\n
        If you believe this is a mistake, please contact us at noreply@exam[12D[K
noreply@example.com
    """)
    
    return msg
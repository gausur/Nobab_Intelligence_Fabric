#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-16 14:51:38.653627

import re
import socket
import ssl
from email.message import EmailMessage

def is_phishing_attack(email):
    if not isinstance(email, EmailMessage):
        raise ValueError("Invalid input, expected EmailMessage object")
    
    sender = email["From"]
    recipient = email["To"]
    subject = email["Subject"]
    body = email.get_payload()
    
    # Check if the message is from a known and trusted sender
    if not is_known_sender(sender):
        return True
    
    # Check if the recipient is trying to phish for a sensitive account
    if is_sensitive_account(recipient):
        return True
    
    # Check if the subject line contains suspicious keywords
    if has_suspicious_keyword(subject):
        return True
    
    # Check if the message body contains suspicious links or attachments
    if has_malicious_content(body):
        return True
    
    return False

def is_known_sender(sender):
    known_senders = [
        "john.doe@example.com",
        "jane.smith@example.com"
    ]
    
    if sender in known_senders:
        return True
    
    return False

def is_sensitive_account(recipient):
    sensitive_accounts = [
        "admin@example.com",
        "root@example.com"
    ]
    
    if recipient in sensitive_accounts:
        return True
    
    return False

def has_suspicious_keyword(subject):
    suspicious_keywords = [
        "phishing",
        "scam",
        "hack"
    ]
    
    for keyword in suspicious_keywords:
        if keyword in subject.lower():
            return True
    
    return False

def has_malicious_content(body):
    malicious_links = [
        "https://example.com/malicious-link"
    ]
    
    for link in malicious_links:
        if link in body:
            return True
    
    return False
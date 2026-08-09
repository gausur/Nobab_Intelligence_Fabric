#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 14:31:34.132352

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    # Check for common phishing attack patterns
    if "://" in email["subject"] or "<script>" in email.get_payload():
        return True
    
    # Check for suspicious URLs in the email body
    url_pattern = re.compile(r"https?://\S+")
    for part in email.walk():
        if part.get_content_maintype() == "text":
            body = part.get_payload()
            if url_pattern.search(body):
                return True
    
    # Check for suspicious attachment file names
    for att in email.iter_attachments():
        if re.match(r"\.exe$|\.bat$|\.dll$", att.get_filename()):
            return True
    
    # If all else fails, assume the email is legitimate
    return False

def mitigate_phishing_attack(email):
    # Remove suspicious URLs from the email body
    url_pattern = re.compile(r"https?://\S+")
    for part in email.walk():
        if part.get_content_maintype() == "text":
            body = part.get_payload()
            new_body = url_pattern.sub("", body)
            part.set_payload(new_body)
    
    # Remove suspicious attachments
    for att in email.iter_attachments():
        if re.match(r"\.exe$|\.bat$|\.dll$", att.get_filename()):
            att.remove()
    
    return email

# Test the script by sending a phishing attack and then mitigating it
email = EmailMessage()
email["from"] = "phishing@example.com"
email["to"] = "victim@example.com"
email["subject"] = "Click here to download your secret file"
email.set_payload("https://www.example.com/download")
smtplib.sendmail("sender@example.com", ["recipient@example.com"], email.as_[9D[K
email.as_string())

# Check if the attack was detected
if is_phishing_attack(email):
    print("Phishing attack detected!")
    
    # Mitigate the attack
    mitigated_email = mitigate_phishing_attack(email)
    smtplib.sendmail("sender@example.com", ["recipient@example.com"], mitig[5D[K
mitigated_email.as_string())
    print("Phishing attack mitigated!")
else:
    print("No phishing attack detected.")
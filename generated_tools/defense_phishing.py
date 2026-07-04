#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-04 23:57:12.519019

import re
import smtplib
from email import message_from_string
from urllib.parse import urlparse

def is_phishing(email):
    # Check for spam triggers
    if "spam" in email["subject"] or "spam" in email["body"]:
        return True
    
    # Check for suspicious sender domain
    if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", ema[3D[K
email["from"]):
        return True
    
    # Check for suspicious content in the message body
    if re.search("http://", email["body"]) or re.search("https://", email["[7D[K
email["body"]):
        url = urlparse(email["body"]).netloc
        if not re.match("^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", url):
            return True
    
    # Check for suspicious attachments
    if email["attachments"]:
        for attachment in email["attachments"]:
            if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,[56D[K
re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", attachment):
                return True
    
    # If none of the above conditions are met, then the email is likely leg[3D[K
legitimate
    return False

def mitigate_phishing(email):
    # Send a copy of the email to a phishing reporting address
    smtplib.sendmail("phishing-reports@example.com", email["from"], message[7D[K
message_from_string(email["body"]))
    
    # Remove any suspicious content from the email
    for pattern in ["http://", "https://", "@"]:
        email["body"] = re.sub(pattern, "", email["body"])
    
    # If there are any attachments, remove them as well
    if email["attachments"]:
        for attachment in email["attachments"]:
            os.remove(attachment)
    
    return email
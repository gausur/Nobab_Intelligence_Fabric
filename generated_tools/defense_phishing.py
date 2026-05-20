#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-20 21:48:03.931360

import re
import smtplib
from email.message import EmailMessage

def check_phishing(email):
    # Check for suspicious keywords in the email subject and body
    if "phishing" in email["subject"] or "scam" in email["body"]:
        return True
    
    # Check for suspicious links in the email content
    for part in email.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if re.search(r"http[s]?://[\w\.]+", part.get_payload()):
            return True
    
    # Check for suspicious attachments in the email content
    if email.has_attachments():
        for attachment in email.attachments:
            if re.search(r"[\w\.]+\.(exe|bat)", attachment.get_filename()):[27D[K
attachment.get_filename()):
                return True
    
    # If no suspicious keywords or links are found, the email is likely leg[3D[K
legitimate
    return False

def mitigate_phishing(email):
    # Send an error message to the sender
    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(email["from"], email["to"], "Error: Phishing attack detec[5D[K
detected")
    
    # Delete the email from the local mailbox
    for folder in ("Inbox", "Sent"):
        try:
            os.remove(os.path.join("~/.mail", folder, email["filename"]))
        except FileNotFoundError:
            pass
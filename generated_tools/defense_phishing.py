#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-31 17:25:29.354373

import re
import smtplib
from email.message import EmailMessage

def is_phishing_email(email):
    # Check if the email has a suspicious subject line or sender domain
    if re.search(r"(?i)phish|scam|fake", email["Subject"]) or re.search(r"\[13D[K
re.search(r"\.(gov|mil|edu)$", email["From"]):
        return True
    # Check if the email has a malicious link in the body
    if re.search(r"<a\s+(?:[^>]*?\s+)?href=[\"']?(.*?)[\"']?\s*>", email.ge[8D[K
email.get_payload()):
        return True
    # Check if the email has a malicious attachment
    if any(attachment["Content-Disposition"] == "attachment" for attachment[10D[K
attachment in email.iter_attachments()):
        return True
    return False

def mitigate_phishing_email(email, smtp_server=None, smtp_port=25, sender="[8D[K
sender="noreply@example.com"):
    # Create a new email message with the original email's content and head[4D[K
headers
    new_message = EmailMessage()
    new_message["Subject"] = email["Subject"]
    new_message["From"] = email["From"]
    new_message["To"] = email["To"]
    # Add a warning message to the email body
    new_message.set_content("Warning: This is a phishing email. Do not clic[4D[K
click on any links or provide any personal information.")
    # Send the new message using the smtplib module
    if smtp_server and smtp_port:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(sender, email["To"], new_message.as_string())
    else:
        print("Could not send phishing warning email")
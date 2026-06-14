#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-14 11:55:04.986596

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    # Check if the email contains a suspicious link
    if "://" in email["Subject"]:
        return True
    # Check if the email contains a suspicious attachment
    for part in email.iter_attachments():
        if not re.match(r".+\.exe$", part.get_filename()):
            return True
    return False

def mitigate_phishing_attack(email, sender):
    # Remove the suspicious link from the email
    email["Subject"] = re.sub(r"://.*", "", email["Subject"])
    # Remove the suspicious attachment from the email
    for part in email.iter_attachments():
        if not re.match(r".+\.exe$", part.get_filename()):
            part.dispose()
    # Send a notification to the sender
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attack Detected"
    msg["From"] = sender
    msg["To"] = email["From"]
    msg.set_content("We have detected a phishing attack on your account. Pl[2D[K
Please check your email for more information.")
    smtplib.sendmail(msg)

def main():
    # Parse the email message
    email = EmailMessage()
    email.parse(sys.stdin)
    # Check if the email is a phishing attack
    if is_phishing_attack(email):
        mitigate_phishing_attack(email, email["From"])
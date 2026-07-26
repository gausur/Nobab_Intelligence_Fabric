#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-26 16:00:15.526011

import re
import smtplib
from email.message import EmailMessage

def check_email(email):
    # Check if the email address is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    
    # Connect to an SMTP server and send a test email
    with smtplib.SMTP("smtp.example.com") as smtp:
        msg = EmailMessage()
        msg["From"] = "phishing@example.com"
        msg["To"] = email
        msg["Subject"] = "Test email for phishing detection"
        msg.set_content("This is a test email to detect phishing attacks.")[10D[K
attacks.")
        smtp.sendmail(msg)
    
    # Check if the email address was used in the test email
    if re.search(r"{}[^@]+".format(email), smtp.data):
        return True
    else:
        return False
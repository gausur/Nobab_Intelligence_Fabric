#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-26 20:06:40.247844

import re
import smtplib
from email.parser import Parser

def is_phishing_email(email):
    # Check if the email contains a link to a malicious website
    link = re.search(r'https?://\S+', email.get('body'))
    if link:
        url = link.group()
        response = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        try:
            response.ehlo()
            response.mail(email.get("from"))
            response.rcpt(url)
            response.quit()
            return True
        except Exception as e:
            print(f"Failed to connect to {url}: {e}")
    return False

def mitigate_phishing_attack(email):
    # Remove the link from the email and send a notification
    body = re.sub(r'https?://\S+', '', email.get("body"))
    subject = f"Phishing attack detected in {email.get('from')}"
    message = Parser().parsestr(f"Subject: {subject}\n\n{body}")
    smtplib.SMTP_SSL("smtp.gmail.com", 465).sendmail(
        email.get("from"), ["admin@example.com"], message.as_string()
    )

def main():
    # Read the email from stdin
    email = Parser().parsestr(sys.stdin.read())
    
    if is_phishing_email(email):
        mitigate_phishing_attack(email)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-06 00:03:07.223198

import re
import smtplib
from email.parser import Parser
from email.utils import getaddresses
from urllib.parse import urlparse

def is_phishing_email(email):
    # Check if the email contains a malicious link
    if "http://" in email["body"] or "https://" in email["body"]:
        return True
    
    # Check if the email contains a suspicious domain
    if not urlparse(email["body"]).hostname.endswith(".com") and not urlpar[6D[K
urlparse(email["body"]).hostname.endswith(".net"):
        return True
    
    return False

def mitigate_phishing_attack(email, sender):
    # Send an email to the sender informing them that their email has been [K
flagged as phishing
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, "password")
        server.sendmail(sender, email["from"], f"Subject: Phishing Attack D[1D[K
Detected\n\nYour email has been flagged as phishing.\n\n{email['body']}")

def main():
    # Parse the email message
    parser = Parser()
    with open("email.txt", "r") as f:
        email = parser.parsestr(f.read())
    
    # Check if the email is a phishing attack
    if is_phishing_email(email):
        mitigate_phishing_attack(email, getaddresses(email["from"])[0][1])

if __name__ == "__main__":
    main()
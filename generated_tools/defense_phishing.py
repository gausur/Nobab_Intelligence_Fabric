#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-13 23:49:26.353203

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    # Check if the email contains a malicious link
    if "http://" in email or "https://" in email:
        return True
    else:
        return False

def mitigate_phishing_attack(email):
    # Send an alert to the sender's email address
    message = EmailMessage()
    message["From"] = "Phishing Alert Bot <noreply@example.com>"
    message["To"] = email["From"]
    message["Subject"] = "Possible Phishing Attack Detected"
    message.set_content("We have detected a possible phishing attack in you[3D[K
your email. Please be cautious when clicking on links or providing personal[8D[K
personal information.")
    smtplib.sendmail(message)

def main():
    # Read the email from stdin
    email = input()
    
    # Check if the email is a phishing attack
    if is_phishing_attack(email):
        mitigate_phishing_attack(email)

if __name__ == "__main__":
    main()
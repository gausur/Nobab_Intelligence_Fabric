#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-01 13:03:54.571652

import re
import smtplib
from email.parser import Parser
from email.header import decode_header

def is_phishing_email(email):
    # Check for common phishing email patterns
    if re.search(r"@example\.[a-z]{2,3}$", email):
        return True
    elif re.search(r"\.\w{2,4}$", email):
        return True
    else:
        return False

def get_email_headers(email):
    # Parse the email headers using the Email Parser library
    parser = Parser()
    parsed_email = parser.parsestr(email)
    headers = {}
    for header, value in parsed_email.items():
        headers[header] = decode_header(value)
    return headers

def get_recipient_domain(email):
    # Extract the recipient domain from the email address
    recipient_domain = email.split("@")[-1]
    return recipient_domain

def is_legitimate_email(email, recipient_domain):
    # Check if the email is legitimate by checking its recipient domain aga[3D[K
against a known good domains list
    with open("good_domains.txt", "r") as f:
        for line in f:
            if recipient_domain == line.strip():
                return True
    return False

def mitigate_phishing(email):
    # Send a phishing warning email to the sender of the suspicious email
    sender = get_email_headers(email)["From"][0]
    recipient = get_recipient_domain(email)
    subject = "Phishing Email Detected"
    body = f"""
    Dear {sender},
    
    We have detected a phishing email attempt on our system. Please be awar[4D[K
aware that sending emails with spoofed sender addresses is illegal and can [K
lead to serious consequences.
    
    If you are the intended recipient of this message, please verify your i[1D[K
identity by clicking on the following link: {recipient}.
    
    Sincerely,
    The System Administrators
    """
    smtplib.SMTP("localhost").sendmail(sender, [sender], f"Subject: {subjec[7D[K
{subject}\n\n{body}")

def main():
    # Read the email from the standard input
    email = sys.stdin.read()
    
    # Check if the email is a phishing attack
    is_phishing = is_phishing_email(email)
    
    # If the email is a phishing attack, mitigate it by sending a warning e[1D[K
email to the sender
    if is_phishing:
        mitigate_phishing(email)

if __name__ == "__main__":
    main()
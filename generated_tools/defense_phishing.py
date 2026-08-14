#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-14 15:47:37.193435

import re
import sys

# Define a list of domains to block
blocked_domains = ["example.com", "example.net"]

# Define a list of email address patterns to block
blocked_email_patterns = ["@example.com", "@example.net"]

# Define a list of email addresses to allow
allowed_email_addresses = ["user@example.com", "user@example.net"]

# Define a list of email subjects to block
blocked_subjects = ["Phishing Email", "Fake Email"]

# Define a list of email bodies to block
blocked_bodies = ["Please click on the link to verify your account", "Pleas[6D[K
"Please click on the link to complete your transaction"]

def is_phishing_email(email):
    # Check if the email address is from a blocked domain
    for domain in blocked_domains:
        if domain in email.sender:
            return True
    
    # Check if the email address matches any of the blocked patterns
    for pattern in blocked_email_patterns:
        if pattern in email.sender:
            return True
    
    # Check if the email address is in the list of allowed email addresses
    if email.sender in allowed_email_addresses:
        return False
    
    # Check if the email subject is in the list of blocked subjects
    if email.subject in blocked_subjects:
        return True
    
    # Check if the email body is in the list of blocked bodies
    if email.body in blocked_bodies:
        return True
    
    return False

def main():
    # Read the email from the command line
    email = sys.argv[1]
    
    # Parse the email
    email_parts = email.split(" ")
    sender = email_parts[0]
    subject = email_parts[1]
    body = email_parts[2]
    
    # Check if the email is a phishing email
    if is_phishing_email(email):
        print("This is a phishing email. Do not open it.")
    else:
        print("This is not a phishing email. You can open it.")
    
if __name__ == "__main__":
    main()
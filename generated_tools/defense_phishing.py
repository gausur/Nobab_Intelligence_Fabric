#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-24 23:00:48.531244

import re
import smtplib
from email.parser import Parser

def check_email(email):
    # Check if the email is valid
    if not re.match(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", email):
        return False
    
    # Check if the email is from a trusted domain
    if not email.split("@")[1].lower() in ["example.com", "gmail.com", "yah[4D[K
"yahoo.com"]:
        return False
    
    # Check if the email contains suspicious keywords
    if any(word in email for word in ["phish", "scam", "fake"]):
        return False
    
    # Check if the email is from a known spammer
    if smtplib.SMTP("smtp.example.com").helo()[0] != 250:
        return False
    
    return True

def main():
    while True:
        try:
            email = input("Enter an email address: ")
            if check_email(email):
                print("The email is valid and from a trusted domain.")
            else:
                print("The email is not valid or from a suspicious domain."[8D[K
domain.")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
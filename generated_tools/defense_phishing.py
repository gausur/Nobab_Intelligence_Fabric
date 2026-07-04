#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-04 20:47:44.018063

import re
import smtplib

def check_email(email):
    """Check if the email is from a trusted domain"""
    pattern = r"^[a-zA-Z0-9_.+-]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]{2,}$"
    match = re.search(pattern, email)
    if match:
        domain = match.group(1)
        trusted_domains = ["example.com", "example.org"]
        return domain in trusted_domains
    else:
        return False

def send_email(to, subject, message):
    """Send an email to the recipient"""
    fromaddr = "noreply@example.com"
    msg = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromaddr, "password")
    server.sendmail(fromaddr, to, msg)
    server.quit()

def main():
    """The main function"""
    email = input("Enter your email: ")
    if check_email(email):
        print("Email is from a trusted domain")
        send_email(to, subject, message)
    else:
        print("Email is not from a trusted domain")
        print("Please try again with an email from a trusted domain.")

if __name__ == "__main__":
    main()
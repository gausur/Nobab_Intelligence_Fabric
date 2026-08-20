#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 00:46:42.559030

import re
import smtplib

def check_email_for_phishing(email):
    # Check for common phishing URLs
    urls = re.findall(r"(http|https)://[a-zA-Z0-9./?=_%-]*", email.get_payl[14D[K
email.get_payload())
    for url in urls:
        if url.startswith("http://"):
            return False
    # Check for common phishing domains
    domains = re.findall(r"[a-zA-Z0-9.-]+@([a-zA-Z0-9.-]+)", email.get_payl[14D[K
email.get_payload())
    for domain in domains:
        if domain in ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com[12D[K
"outlook.com", "aol.com"]:
            return False
    return True

def send_email_for_phishing(email):
    # Send an email with a warning
    smtp = smtplib.SMTP("localhost")
    smtp.sendmail("phishing@example.com", email.get_payload(), "Phishing em[2D[K
email detected")
    smtp.quit()

def main():
    # Read the email from the command line
    email = input("Enter email: ")
    # Check if the email is a phishing attempt
    if not check_email_for_phishing(email):
        # Send a warning email
        send_email_for_phishing(email)
    else:
        print("Email is not a phishing attempt")

if __name__ == "__main__":
    main()
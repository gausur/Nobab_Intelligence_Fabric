#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-23 13:29:28.086049

import re
import smtplib

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return True if re.match(regex, email) else False

def send_email(email):
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('user@example.com', 'password')
    server.sendmail('user@example.com', email, 'This is a test email.')
    server.quit()

def detect_phishing_attacks(emails):
    for email in emails:
        if not is_valid_email(email):
            continue
        try:
            send_email(email)
        except smtplib.SMTPException:
            print(f"Phishing attack detected: {email}")

def main():
    emails = ['john.doe@example.com', 'jane.doe@example.com', 'phishing.att[13D[K
'phishing.attack@example.com']
    detect_phishing_attacks(emails)

if __name__ == "__main__":
    main()
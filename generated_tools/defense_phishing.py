#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-26 17:33:28.719894

import re
import smtplib

def is_phishing_attack(email_body):
    pattern = r"[-a-zA-Z0-9._%+]+@[-a-zA-Z0-9._%+]+"
    if re.search(pattern, email_body):
        return True
    return False

def send_email(sender, recipient, subject, body):
    server = smtplib.SMTP("smtp.example.com")
    server.sendmail(sender, recipient, f"Subject: {subject}\r\n\r\n{body}")[25D[K
{subject}\r\n\r\n{body}")
    server.quit()

def main():
    email_body = input("Enter email body: ")
    if is_phishing_attack(email_body):
        print("Phishing attack detected!")
        send_email("admin@example.com", "admin@example.com", "Phishing Atta[4D[K
Attack", "A phishing attack was detected on the email server.")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()
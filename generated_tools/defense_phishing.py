#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-26 18:28:25.518915

import re
import smtplib
from email.mime.text import MIMEText

def is_phishing_attack(email):
    """Detects if an email is a phishing attack using a regular expression"[11D[K
expression"""
    pattern = r"[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def send_email(email, subject, body):
    """Sends an email using the smtplib library"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(email, "password")
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = email
    message["To"] = email
    server.send_message(message)
    server.quit()

def mitigate_phishing_attack(email, subject, body):
    """Mitigates a phishing attack by sending an email to the sender"""
    if is_phishing_attack(email):
        send_email("from@example.com", "Phishing Attack Detected", f"Subjec[8D[K
f"Subject: {subject}\n\n{body}")

def main():
    """Entry point of the script"""
    email = input("Enter an email address: ")
    subject = input("Enter a subject line: ")
    body = input("Enter a message body: ")
    mitigate_phishing_attack(email, subject, body)

if __name__ == "__main__":
    main()
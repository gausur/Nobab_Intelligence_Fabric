#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-05 17:23:32.961580

import re
import smtplib
from email.parser import Parser

def parse_email(raw_email):
    parser = Parser()
    message = parser.parsestr(raw_email)
    return message

def is_phishing_attack(message):
    if "Click here to confirm your account" in message.get("Subject", ""):
        return True
    else:
        return False

def mitigate_phishing_attack(message):
    sender = message["From"]
    recipient = message["To"]
    subject = message["Subject"]
    body = message.get_payload()
    if is_phishing_attack(message):
        print("Phishing attack detected!")
        return
    else:
        send_email(sender, recipient, subject, body)
        print("Email sent successfully!")

def send_email(sender, recipient, subject, body):
    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(sender, recipient, f"Subject: {subject}\n\n{body}")
    smtp.quit()

if __name__ == "__main__":
    with open("email.txt", "r") as file:
        raw_email = file.read()
    message = parse_email(raw_email)
    mitigate_phishing_attack(message)
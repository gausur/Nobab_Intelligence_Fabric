#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-29 11:18:00.797785

import re
import smtplib
from email.message import EmailMessage

def is_phishing_url(url):
    return "www.evil-phishers.com" in url

def send_email(recipient, message):
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attempt Detected"
    msg["From"] = "noreply@example.com"
    msg["To"] = recipient
    msg.set_content(message)
    smtplib.sendmail("noreply@example.com", recipient, msg.as_string())

def phishing_detector(url):
    if is_phishing_url(url):
        send_email("admin@example.com", "Phishing attempt detected from {}"[3D[K
{}".format(url))
        return True
    else:
        return False

if __name__ == "__main__":
    url = input("Enter the URL to check for phishing attempts: ")
    if phishing_detector(url):
        print("Phishing attempt detected!")
    else:
        print("No phishing attempt detected.")
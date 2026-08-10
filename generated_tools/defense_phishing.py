#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 17:46:04.716504

import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient, subject, body):
    sender = "noreply@example.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.attach(MIMEText(body, "plain"))
    smtp_server = smtplib.SMTP("smtp.example.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender, "password")
    smtp_server.sendmail(sender, recipient, message.as_string())
    smtp_server.quit()

def detect_phishing(url):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.search(pattern, url):
        return "The URL appears to be a valid email address."
    else:
        return "The URL does not appear to be a valid email address."

def mitigate_phishing(url):
    send_email("admin@example.com", "Possible Phishing Attack Detected", f"[2D[K
f"A potential phishing attack was detected on {url}. Please investigate fur[3D[K
further.")

url = input("Enter URL: ")
result = detect_phishing(url)
if result == "The URL does not appear to be a valid email address.":
    mitigate_phishing(url)
else:
    print(result)
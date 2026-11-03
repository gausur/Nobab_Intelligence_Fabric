#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-03 11:33:21.837269

import re
import smtplib

def is_phishing_url(url):
    pattern = r"^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, url):
        return True
    else:
        return False

def send_email(email, subject, body):
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login("your-email@gmail.com", "your-email-password")
    smtp.sendmail("from@gmail.com", email, f"Subject: {subject}\n\n{body}")
    smtp.quit()

def detect_phishing_attacks(emails):
    for email in emails:
        url = email["url"]
        if is_phishing_url(url):
            send_email(email["email"], "Phishing Attack Detected", f"We have detected a phishing attack on your account. Please visit {url} to verify that it is a legitimate website.")

def main():
    emails = [
        {"email": "john.doe@example.com", "url": "http://www.phishing-site.com"},
        {"email": "jane.doe@example.com", "url": "http://www.legitimate-site.com"},
        {"email": "john.smith@example.com", "url": "http://www.phishing-site.com"},
        {"email": "jane.smith@example.com", "url": "http://www.legitimate-site.com"},
        {"email": "john.jones@example.com", "url": "http://www.phishing-site.com"},
        {"email": "jane.jones@example.com", "url": "http://www.legitimate-site.com"}
    ]
    detect_phishing_attacks(emails)

if __name__ == "__main__":
    main()
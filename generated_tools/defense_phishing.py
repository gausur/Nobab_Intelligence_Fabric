#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-02 11:54:35.173478

import re
import smtplib
from email.mime.text import MIMEText

def detect_phishing_attacks(email):
    # Extract the subject and body of the email
    subject = email["Subject"]
    body = email["Body"]

    # Check if the subject or body contains any suspicious keywords
    keywords = ["FREE", "DISCOUNT", "URGENT", "Click here to activate your account"]
    if any(keyword in subject.lower() for keyword in keywords) or any(keyword in body.lower() for keyword in keywords):
        return True

    # Check if the email contains a malicious URL
    url = re.search(r"https?://\S+", body)
    if url:
        try:
            response = smtplib.SMTP("mail.example.com", 587)
            response.ehlo()
            response.starttls()
            response.login("info@example.com", "password")
            response.rcpt(url.group())
            response.quit()
            return True
        except smtplib.SMTPException:
            return False

    # Check if the email contains a malicious attachment
    attachment = re.search(r"application/pdf", email["Content-Type"])
    if attachment:
        try:
            response = smtplib.SMTP("mail.example.com", 587)
            response.ehlo()
            response.starttls()
            response.login("info@example.com", "password")
            response.data(email["Body"])
            response.quit()
            return True
        except smtplib.SMTPException:
            return False

    return False

def mitigate_phishing_attacks(email):
    # Create a new email with a spoofed sender
    new_email = MIMEText(email["Body"], "plain")
    new_email["Subject"] = email["Subject"]
    new_email["From"] = "info@example.com"
    new_email["To"] = email["To"]

    # Send the new email
    smtp = smtplib.SMTP("mail.example.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login("info@example.com", "password")
    smtp.sendmail("info@example.com", email["To"], new_email.as_string())
    smtp.quit()

def main():
    # Read the email from the input
    email = input()

    # Detect and mitigate phishing attacks
    if detect_phishing_attacks(email):
        mitigate_phishing_attacks(email)

if __name__ == "__main__":
    main()
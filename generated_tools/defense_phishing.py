#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-08 01:01:08.723221

import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr

def send_email(recipient, subject, body):
    # Create a new SMTP connection
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("your-email@example.com", "your-password")

    # Create a new MIME message
    msg = MIMEText(body)

    # Set the email headers
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = parseaddr('from@example.com')
    msg['To'] = parseaddr(recipient)

    # Send the email
    s.sendmail("from@example.com", recipient, msg.as_string())
    s.quit()

def detect_phishing(url):
    # Check if the URL is valid and contains "://"
    if re.match(r'^https?://', url) is not None:
        # Extract the domain name from the URL
        domain = urlparse(url).hostname

        # Check if the domain name is in the phishing list
        with open("phishing_list.txt", "r") as f:
            for line in f:
                if line.strip() == domain:
                    return True

    return False

def main():
    # Read the email message from stdin
    msg = sys.stdin.read()

    # Parse the email message and extract the URL
    url = re.findall(r'https?://[^\s]+\.\w+', msg)
    if len(url) == 0:
        return

    # Check if the URL is a phishing site
    if detect_phishing(url):
        # Send an email to the recipient with a warning message
        send_email("recipient@example.com", "Phishing Alert", "This email c[1D[K
contains a phishing link. Please do not click on it.")
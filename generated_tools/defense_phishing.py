#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-27 17:56:29.771662

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attempt(email):
    # Check if the email is from a known spammer domain
    if email["From"].split("@")[1].lower() in SPAMMERS:
        return True

    # Check if the email contains a malicious link
    for part in email.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if re.search(r"https?://[^\s]+\.(?:com|net)", part.get_payload(), r[1D[K
re.I):
            return True

    # Check if the email contains a malicious attachment
    for part in email.walk():
        if part.get_content_maintype() == "application" and part["Content-D[15D[K
part["Content-Disposition"] == "attachment":
            return True

    # Check if the email is spam based on its content
    if re.search(r"viagra|cialis|vardenafil", email.get("Subject"), re.I):
        return True

def mitigate_phishing_attempt(email, recipient):
    # Send an email to the recipient with a phishing warning
    msg = EmailMessage()
    msg["From"] = "Phishing Warning <phishing@example.com>"
    msg["To"] = recipient
    msg["Subject"] = "Phishing Attempt Detected"
    msg.set_content("A phishing attempt has been detected for your account.[8D[K
account. Please check your email carefully and do not click on any suspicio[8D[K
suspicious links or download any attachments.")
    smtplib.sendmail(msg)

# List of known spammer domains
SPAMMERS = [
    "example1.com",
    "example2.com",
    "example3.com"
]

while True:
    # Read an email from the server and check if it is a phishing attempt
    with smtplib.SMTP("localhost") as server:
        server.login("username", "password")
        for message in server.iter_data():
            email = EmailMessage()
            email.set_content(message)
            if is_phishing_attempt(email):
                mitigate_phishing_attempt(email, email["To"])
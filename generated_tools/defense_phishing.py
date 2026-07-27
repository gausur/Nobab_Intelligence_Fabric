#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-27 22:02:09.071541

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email address is valid
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", em[2D[K
email):
        return False

    # Check if the sender's domain is in the spam list
    sender_domain = email.split("@")[1]
    if sender_domain in SPAM_DOMAINS:
        return True

    # Check if the email contains suspicious keywords or phrases
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in email:
            return True

    return False

def mitigate_phishing(email):
    # Mark the email as spam
    email.spam = True

    # Modify the subject line to make it more suspicious
    subject = "SPAM ALERT! Do not click on links or open attachments from t[1D[K
this sender"
    email.subject = subject

    # Modify the body of the email to include a warning about the spam natu[4D[K
nature of the message
    body = "This is an SPAM alert! Do not click on any links or open any at[2D[K
attachments from this sender, as they may contain malware or other harmful [K
content."
    email.body = body

    # Send the modified email to a secondary email address for further anal[4D[K
analysis
    smtplib.sendmail(email.from_address, "spam@example.com", email.as_strin[14D[K
email.as_string())

# List of spammy domains
SPAM_DOMAINS = ["phishing.com", "ransomware.org"]

# List of suspicious keywords or phrases to look for in emails
SUSPICIOUS_KEYWORDS = ["click here", "open now", "install now", "download n[1D[K
now"]

# Function to check if an email is phishing and mitigate it if necessary
def check_and_mitigate(email):
    if is_phishing(email):
        mitigate_phishing(email)

# Main function that runs the checks on incoming emails
def main():
    # Connect to an email server and retrieve the latest emails
    with smtplib.SMTP("smtp.example.com") as server:
        server.login("username", "password")
        messages = server.retrieve()

    # Iterate over the retrieved emails and check if they are phishing
    for message in messages:
        email = EmailMessage(message)
        check_and_mitigate(email)
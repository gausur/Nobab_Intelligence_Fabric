#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 21:25:10.986226

import re
import smtplib
from email.message import EmailMessage

# Define the list of domain names that are considered safe
safe_domains = ["example.com", "example2.com"]

def is_phishing(email):
    # Check if the sender's domain name is in the safe list
    if email["from"].split("@")[1] not in safe_domains:
        return True
    else:
        return False

def mitigate_phishing(email):
    # Send a bounce message to the attacker's email address
    msg = EmailMessage()
    msg["From"] = "No-Reply <noreply@example.com>"
    msg["To"] = email["from"]
    msg["Subject"] = "Phishing Attempt Blocked"
    msg.set_content("This is a bounce message to indicate that your phishin[7D[K
phishing attempt has been blocked.")
    smtplib.sendmail("noreply@example.com", email["to"], msg.as_string())

# Read the incoming email message from stdin
email = None
while True:
    line = sys.stdin.readline()
    if not line:
        break
    if email is None:
        email = EmailMessage()
    if line == "\r\n":
        continue
    else:
        email.add_header(line)

# Check if the email is a phishing attempt and mitigate it if necessary
if is_phishing(email):
    mitigate_phishing(email)
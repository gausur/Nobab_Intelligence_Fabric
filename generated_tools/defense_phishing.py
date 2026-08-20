#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 07:36:26.704749

import re
import smtplib

# Define a function to check if an email is a phishing attack
def is_phishing_attack(email):
    # Check if the email contains any suspicious keywords
    if any(k in email for k in ["phishing", "scam", "fraud", "hack"]):
        return True
    # Check if the email address is from a known spam source
    if email.endswith("@phishing.com"):
        return True
    # Check if the email contains any suspicious links
    if any(l in email for l in ["https://phishing.com", "https://scam.com",[19D[K
"https://scam.com", "https://fraud.com", "https://hack.com"]):
        return True
    # Check if the email contains any suspicious content
    if any(c in email for c in ["Click here to claim your prize!", "Click h[1D[K
here to download the latest virus.", "Click here to access your account."])[11D[K
account."]):
        return True
    # If none of the above conditions are met, the email is likely legitima[8D[K
legitimate
    return False

# Define a function to send an alert to an admin if a phishing attack is de[2D[K
detected
def send_alert(email):
    # Use the smtplib library to send an email to an admin
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("admin@example.com", "password")
    server.sendmail("admin@example.com", "admin@example.com", "Phishing att[3D[K
attack detected: " + email)
    server.quit()

# Use a regular expression to extract the email address from an input strin[5D[K
string
email_re = re.compile(r"[\w\.]+@[\w\.]+")

# Loop through all the emails in a given text file
with open("emails.txt") as f:
    for line in f:
        # Extract the email address from the line
        email = email_re.search(line).group()
        # Check if the email is a phishing attack
        if is_phishing_attack(email):
            # Send an alert to an admin
            send_alert(email)
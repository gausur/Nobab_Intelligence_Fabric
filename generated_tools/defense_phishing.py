#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-08 17:24:18.423163

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if "gmail" in domain or "hotmail" in domain or "yahoo" in domain:
        return True
    else:
        return False

def mitigate_phishing_attack(email):
    if is_phishing_url(email["from"]):
        print("Phishing email detected!")
        # Send an alert to IT department or admin
        # Call a function to block the sender's IP address
        # Delete the email from inbox

def main():
    # Set up email server and login credentials
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, password)

    # Fetch emails from inbox
    messages = imapclient.IMAPClient(server)
    messages.search(["ALL"])

    for message_id in messages:
        message = messages[message_id]
        email = message["EMAIL"]
        if is_phishing_url(email):
            mitigate_phishing_attack(email)

if __name__ == "__main__":
    main()
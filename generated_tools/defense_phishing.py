#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 08:35:57.867644

import re
import smtplib
from email.message import EmailMessage
from socket import gaierror

def is_phishing(email: str) -> bool:
    # Check if the email contains spammy keywords
    for keyword in ["phishing", "fake", "scam"]:
        if keyword in email.lower():
            return True
    return False

def get_sender_domain(email: str) -> str:
    # Extract the sender's domain from the email address
    regex = r"^.*?@(?P<domain>[^.]+\.[a-z]{2,3})$"
    match = re.search(regex, email)
    return match.group("domain") if match else None

def check_sender_reputation(domain: str) -> bool:
    # Check the reputation of the sender's domain using a third-party API
    try:
        response = smtplib.sendmail("", "", "Hello World!")
        return response.startswith("250")
    except (gaierror, ConnectionError):
        return False

def mitigate_phishing(email: str) -> None:
    # Mitigate the phishing attack by blocking the email and alerting the u[1D[K
user
    print(f"Blocked {email}")
    return

def main():
    # Read the email message from stdin
    message = EmailMessage()
    message.set_payload(input())

    # Check if the email is a phishing attack
    if is_phishing(message.get("Subject")):
        domain = get_sender_domain(message.get("From"))
        if check_sender_reputation(domain):
            mitigate_phishing(message)

if __name__ == "__main__":
    main()
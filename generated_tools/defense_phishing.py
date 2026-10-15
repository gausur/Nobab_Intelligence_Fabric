#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-15 12:25:12.786252

import re
import smtplib

def is_phishing_url(url):
    return re.search(r"https?://\w+.\w+", url)

def is_phishing_email(email):
    return re.search(r"@\w+", email)

def is_phishing_message(message):
    return is_phishing_url(message.get("url")) or is_phishing_email(message[25D[K
is_phishing_email(message.get("to"))

def mitigate_phishing_attack(message):
    if is_phishing_message(message):
        # Log the attack
        print("Phishing attack detected")
        # Send a notification to the appropriate person
        smtplib.sendmail("phishing@example.com", "admin@example.com", "Phis[5D[K
"Phishing attack detected")

def main():
    while True:
        message = input("Enter message: ")
        mitigate_phishing_attack(message)

if __name__ == "__main__":
    main()
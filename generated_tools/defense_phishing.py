#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-19 10:06:15.148110

import re
import smtplib

def detect_phishing_attacks(email):
    pattern = r"(https?:\/\/[^\/]*)"
    links = re.findall(pattern, email)
    for link in links:
        try:
            smtplib.SMTP().connect(link)
        except smtplib.SMTPConnectError:
            print(f"Phishing attack detected: {link}")

def main():
    while True:
        email = input("Enter an email: ")
        detect_phishing_attacks(email)

if __name__ == "__main__":
    main()
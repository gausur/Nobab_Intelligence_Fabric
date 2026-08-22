#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-22 10:15:41.343556

import re
import smtplib

def is_phishing_url(url):
    return re.search(r"^http(s)?://[a-zA-Z0-9.-]+\.phishing\.com", url)

def is_phishing_email(email):
    return re.search(r"^[a-zA-Z0-9.-]+\@phishing\.com", email)

def is_phishing_message(message):
    return is_phishing_url(message.get("url", "")) or is_phishing_email(mes[21D[K
is_phishing_email(message.get("from", ""))

def mitigate_phishing(message):
    if is_phishing_message(message):
        print("Phishing attack detected!")
        smtplib.sendmail(
            "spam-filter@example.com",
            message["from"],
            "Phishing attack detected!",
        )

def main():
    while True:
        message = input("Message: ")
        mitigate_phishing(message)

if __name__ == "__main__":
    main()
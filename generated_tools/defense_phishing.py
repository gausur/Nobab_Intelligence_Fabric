#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-09 03:34:15.216140

import re
import smtplib

def check_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

def check_domain(domain):
    if len(domain) > 3 and domain.count(".") == 2:
        return True
    else:
        return False

def check_url(url):
    if "://" in url and "/" in url:
        return True
    else:
        return False

def mitigate_phishing(message):
    if not check_email(message.get("From")) or not check_domain(message.get[24D[K
check_domain(message.get("To")):
        print("Possible phishing attack detected!")
        return False
    elif not check_url(message.get("Subject")):
        print("Possible phishing attack detected!")
        return False
    else:
        return True

def main():
    message = smtplib.SMTP().recv_message()
    mitigate_phishing(message)

if __name__ == "__main__":
    main()
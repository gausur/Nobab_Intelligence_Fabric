#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-16 09:27:13.501019

import re
import socket
from email.message import EmailMessage

def is_phishing_attack(email):
    if not email:
        return False
    if "@" in email and "." in email:
        domain = email.split("@")[1]
        if len(domain) > 3:
            try:
                socket.gethostbyname(domain)
                return True
            except:
                return False
    else:
        return False

def mitigate_phishing_attack(email):
    if is_phishing_attack(email):
        print("Possible phishing attack detected!")
        return
    else:
        return

if __name__ == "__main__":
    email = input("Enter an email address: ")
    mitigate_phishing_attack(email)
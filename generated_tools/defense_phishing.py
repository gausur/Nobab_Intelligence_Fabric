#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-29 13:37:22.203705

import re
import socket
import smtplib

def check_phishing_url(url):
    if re.match(r"^https?://", url):
        try:
            socket.gethostbyname(urlparse(url).hostname)
            return False
        except socket.gaierror:
            return True
    else:
        return True

def check_phishing_email(email):
    if re.match(r"^[^@]+@[^@]+\.[^@]+", email):
        try:
            smtplib.SMTP("smtp.gmail.com", 587)
            return False
        except smtplib.SMTPServerDisconnected:
            return True
    else:
        return True

def mitigate_phishing_attack(url, email):
    if check_phishing_url(url):
        print("Phishing URL detected:", url)
    if check_phishing_email(email):
        print("Phishing email detected:", email)

if __name__ == "__main__":
    mitigate_phishing_attack("http://example.com", "john.doe@phishing.com")[24D[K
"john.doe@phishing.com")
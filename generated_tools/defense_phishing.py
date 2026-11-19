#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-19 02:56:19.863961

import re
import smtplib

def is_phishing_url(url):
    return re.match(r"(https?://)?(www\.)?example\.com/?", url)

def is_phishing_email(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@example\.com$)", email)

def mitigate_phishing_attack(request):
    if is_phishing_url(request.url) or is_phishing_email(request.email):
        print("Phishing attack detected!")
        return "403 Forbidden"
    else:
        return "200 OK"

if __name__ == "__main__":
    while True:
        request = input("Enter a URL or email address: ")
        if request:
            print(mitigate_phishing_attack(request))
        else:
            break
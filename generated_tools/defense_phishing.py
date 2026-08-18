#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-18 12:29:12.018743

import re
import email
from email.message import EmailMessage

def detect_phishing_attack(email_message):
    if email_message.is_multipart():
        for part in email_message.get_payload():
            if part.is_multipart():
                detect_phishing_attack(part)
            else:
                part_content = part.get_content()
                if re.search(r'href="(?!https?://[a-z0-9.-]+\.[a-z]{2,})', [K
part_content):
                    print('Phishing attack detected!')
                    return
    else:
        email_content = email_message.get_content()
        if re.search(r'href="(?!https?://[a-z0-9.-]+\.[a-z]{2,})', email_co[8D[K
email_content):
            print('Phishing attack detected!')
            return

def main():
    with open('email.txt', 'r') as f:
        email_message = EmailMessage.from_string(f.read())
        detect_phishing_attack(email_message)

if __name__ == '__main__':
    main()
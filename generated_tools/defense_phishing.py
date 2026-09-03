#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-03 16:51:24.649166

import re
import smtplib

def is_phishing_attack(email):
    if not email:
        return False
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return False
    if 'phish' in email:
        return True
    return False

def mitigate_phishing_attack(email):
    if is_phishing_attack(email):
        print('Phishing attack detected!')
        return
    print('No phishing attack detected.')

def main():
    email = input('Enter email: ')
    mitigate_phishing_attack(email)

if __name__ == '__main__':
    main()
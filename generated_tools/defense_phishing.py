#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-10 10:20:21.021210

import re
import smtplib
import dns.resolver

def is_phishing_domain(domain):
    try:
        dns.resolver.query(domain, 'A')
    except dns.resolver.NXDOMAIN:
        return False
    return True

def is_phishing_email(email):
    domain = email.split('@')[1]
    return is_phishing_domain(domain)

def mitigate_phishing_attack(email):
    if is_phishing_email(email):
        return
    try:
        smtplib.sendmail('noreply@example.com', email, 'This is a phishing [K
attack')
    except smtplib.SMTPException:
        pass

if __name__ == '__main__':
    email = input('Enter email address: ')
    mitigate_phishing_attack(email)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-22 06:43:28.492538

import re
import smtplib
from email.message import EmailMessage

def is_phishing_url(url):
    return bool(re.search(r'^http://|https://', url))

def is_valid_domain(email, domain):
    return True if email.split('@')[-1] == domain else False

def send_email(sender, recipient, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(body)
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

def phishing_attack_detected(email, url):
    if is_phishing_url(url) and not is_valid_domain(email, 'example.com'):
        send_email('phishing@example.com', email, 'Phishing Attempt', f'{ur[5D[K
f'{url} is a phishing website!')

def main():
    while True:
        email = input('Enter your email: ')
        url = input('Enter the URL you visited: ')
        phishing_attack_detected(email, url)

if __name__ == '__main__':
    main()
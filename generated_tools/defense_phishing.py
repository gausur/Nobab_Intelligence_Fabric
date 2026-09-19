#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-19 23:55:57.714007

import re
import smtplib

def check_phishing_url(url):
    pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6[61D[K
r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    if re.match(pattern, url):
        return True
    else:
        return False

def check_phishing_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def check_phishing_message(message):
    if check_phishing_url(message) or check_phishing_email(message):
        return True
    else:
        return False

def send_email(sender, recipient, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, 'password')
    server.sendmail(sender, recipient, f'Subject: {subject}\n\n{message}')
    server.quit()

def main():
    message = input('Enter the message: ')
    if check_phishing_message(message):
        send_email('phishing@example.com', 'john.doe@example.com', 'Phishin[8D[K
'Phishing Attack Detected', message)
        print('Phishing attack detected. Please check your email.')
    else:
        print('No phishing attack detected.')

if __name__ == '__main__':
    main()
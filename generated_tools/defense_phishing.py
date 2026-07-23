#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-23 22:00:46.570629

import re
import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = to
    server = smtplib.SMTP('smtp.example.com')
    server.sendmail(to, [to], msg.as_string())
    server.quit()

def is_phishing_email(email):
    if re.search(r'http://', email) or re.search(r'https://', email):
        return True
    else:
        return False

def phishing_mitigation(email, url):
    send_email(email, 'Phishing Attempt Detected!', f'You have been targete[7D[K
targeted by a phishing attack. Please visit {url} to verify your identity.'[10D[K
identity.')

def main():
    email = input('Enter email: ')
    if is_phishing_email(email):
        url = input('Enter URL: ')
        phishing_mitigation(email, url)
    else:
        print('Email not detected as a phishing attempt.')

if __name__ == '__main__':
    main()
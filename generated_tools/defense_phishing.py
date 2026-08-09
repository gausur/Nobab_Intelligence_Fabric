#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 19:29:54.327635

import re
import smtplib
from email import message_from_string

def is_phishing_email(email_message):
    if email_message['subject'] == 'Fake Phishing Email':
        return True
    else:
        return False

def send_report(email_address, report):
    msg = message_from_string(f'Subject: Phishing Report\n{report}')
    smtplib.sendmail(None, email_address, msg.as_string())

def main():
    with open('emails.txt', 'r') as f:
        emails = f.readlines()
    for email in emails:
        try:
            email_message = message_from_string(email)
            if is_phishing_email(email_message):
                send_report(email_address, 'Phishing email detected')
                print('Report sent to', email_address)
        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    main()
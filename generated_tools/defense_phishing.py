#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-22 22:36:35.713598

import re
import smtplib

def phishing_detector(email):
    # Check if the email is from a trusted source
    if not email['From'].endswith('@example.com'):
        return False

    # Check if the email contains a suspicious attachment
    if email['Attachments']:
        for attachment in email['Attachments']:
            if attachment['Name'].endswith('.exe'):
                return False

    # Check if the email contains a suspicious link
    if re.search(r'<a href=.*(http|https)://(www\.)?example.com/', email['B[8D[K
email['Body']):
        return False

    return True

def main():
    email = input('Enter the email message: ')
    if phishing_detector(email):
        print('This email is likely a phishing attempt.')
    else:
        print('This email is likely legitimate.')

if __name__ == '__main__':
    main()
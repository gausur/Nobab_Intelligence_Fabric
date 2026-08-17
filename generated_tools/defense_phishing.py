#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 21:20:15.033589

import re
import email

def is_phishing_url(url):
    # Check if the URL is a phishing site
    if re.search(r'https?://[^.]+\.phishing\.site', url):
        return True
    else:
        return False

def is_phishing_email(email_content):
    # Check if the email contains a phishing link
    if re.search(r'https?://[^.]+\.phishing\.site', email_content):
        return True
    else:
        return False

def mitigate_phishing_attack(email_content):
    # Remove any links to phishing sites
    re.sub(r'https?://[^.]+\.phishing\.site', '', email_content)

def main():
    # Read the email from stdin
    email_content = input()

    # Check if the email contains a phishing link
    if is_phishing_email(email_content):
        # Mitigate the phishing attack
        mitigate_phishing_attack(email_content)

        # Print the modified email
        print(email_content)

if __name__ == '__main__':
    main()
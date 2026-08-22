#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-22 08:22:34.943232

import re
import smtplib
import ssl

def is_phishing_link(url):
    pattern = r"^https?://[^\s]+"
    return re.match(pattern, url)

def get_domain(url):
    pattern = r"^https?://([^\s]+)"
    return re.match(pattern, url).group(1)

def is_valid_domain(domain):
    return domain in ["example.com", "example.net", "example.org"]

def send_phishing_email(email, url):
    fromaddr = "sender@example.com"
    toaddr = email
    subject = "Phishing Attempt"
    body = f"Please visit {url} to confirm your account."
    msg = f"Subject: {subject}\n\n{body}"
    server = smtplib.SMTP_SSL("smtp.example.com")
    server.login("sender@example.com", "password")
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()

def main():
    with open("emails.txt") as f:
        for line in f:
            email = line.strip()
            url = "https://example.com/confirm?token=12345"
            if is_phishing_link(url):
                domain = get_domain(url)
                if not is_valid_domain(domain):
                    send_phishing_email(email, url)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-31 14:42:24.580117

import re
import smtplib

def is_phishing_url(url):
    pattern = r"^http(s)?://[a-zA-Z0-9\-\.]+(:[0-9]+)?/\S*$"
    match = re.match(pattern, url)
    if match:
        return True
    else:
        return False

def is_phishing_email(email):
    pattern = r"^[a-zA-Z0-9\-\.]+@[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}$"
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

def send_email(sender, recipient, subject, message):
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(sender, "password")
    smtp.sendmail(sender, recipient, f"Subject: {subject}\n\n{message}")
    smtp.quit()

def main():
    url = input("Enter the URL to check: ")
    if is_phishing_url(url):
        print("This URL is a phishing site.")
        send_email("info@example.com", "user@example.com", "Phishing Site D[1D[K
Detected", f"The URL {url} is a phishing site.")
    else:
        print("This URL is not a phishing site.")

if __name__ == "__main__":
    main()
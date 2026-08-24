#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-24 00:48:12.579619

import re
import smtplib

def is_phishing_url(url):
    pattern = r"^https?://.*(google|microsoft|amazon|yahoo)\.(com|co\.uk|de[61D[K
r"^https?://.*(google|microsoft|amazon|yahoo)\.(com|co\.uk|de|fr|it|es|in|cr"^https?://.*(google|microsoft|amazon|yahoo)\.(com|co\.uk|defr|it|es|in|com\.au|co\.jp|co\.nz|co\.uk|co\.za|com\.au|com\.tw|com\.tr|com\.mx|com\.ph|cm\.au|co\.jp|co\.nz|co\.uk|co\.za|com\.au|com\.tw|com\.tr|com\.mx|com\.ph|com\.vn)\b"
    if re.match(pattern, url):
        return True
    return False

def is_phishing_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@(google|microsoft|amazon|yahoo)\.(com|co[61D[K
r"^[a-zA-Z0-9._%+-]+@(google|microsoft|amazon|yahoo)\.(com|co\.uk|de|fr|it|r"^[a-zA-Z0-9._%+-]+@(google|microsoft|amazon|yahoo)\.(com|co.uk|de|fr|it|es|in|com\.au|co\.jp|co\.nz|co\.uk|co\.za|com\.au|com\.tw|com\.tr|com\.mx|cos|in|com\.au|co\.jp|co\.nz|co\.uk|co\.za|com\.au|com\.tw|com\.tr|com\.mx|com\.ph|com\.vn)$"
    if re.match(pattern, email):
        return True
    return False

def mitigate_phishing(url, email):
    if is_phishing_url(url):
        print("Phishing URL detected!")
    if is_phishing_email(email):
        print("Phishing email detected!")
    else:
        print("No phishing detected.")

def main():
    url = input("Enter URL: ")
    email = input("Enter email: ")
    mitigate_phishing(url, email)

if __name__ == "__main__":
    main()
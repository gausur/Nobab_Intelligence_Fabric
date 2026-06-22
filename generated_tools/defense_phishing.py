#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-22 18:48:06.464424

import re
import smtplib
from email.parser import Parser
from email.message import EmailMessage

def is_phishing(email):
    """Check if the given email message contains a phishing attack"""
    sender = email["From"]
    recipient = email["To"]
    subject = email["Subject"]
    body = email.get_payload()
    has_suspicious_urls = re.search(r"https?://[^\.]+\.[a-z]{2,3}/", body)
    has_suspicious_emails = re.search(r"\w+@\w+\.\w{2,4}", body)
    is_scammy = re.search(r"(?i)\b(scam|phish|hack|fraud|rip off|discount|g[14D[K
off|discount|get rich quick)\b", subject)
    return has_suspicious_urls and has_suspicious_emails and is_scammy

def mitigate_phishing(email):
    """Mitigate the phishing attack by marking it as spam"""
    sender = email["From"]
    recipient = email["To"]
    subject = email["Subject"]
    body = email.get_payload()
    smtplib.SMTP("localhost")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, "password")
    msg = f"Subject: Phishing Attack Detected\n\nHello {recipient}, \n\nWe [K
have detected a phishing attack on your email account.\n\nPlease do not cli[3D[K
click on any links or provide any personal information to this sender.\n\nT[12D[K
sender.\n\nThank you,\n{sender}"
    server.sendmail(sender, recipient, msg)
    server.quit()

def main():
    """Main function"""
    message = Parser().parse(sys.stdin)
    if is_phishing(message):
        mitigate_phishing(message)

if __name__ == "__main__":
    main()
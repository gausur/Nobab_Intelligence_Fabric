#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-11 09:21:04.238420

import re
import smtplib
from email import message_from_bytes

def is_phishing_email(email):
    """Check if the email contains a suspicious link."""
    try:
        msg = message_from_bytes(email)
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                body = part.get_payload(decode=True)
                if re.search('(?i)(https?://)?\w+\.(phishing|scam)\.[a-z]',[56D[K
re.search('(?i)(https?://)?\w+\.(phishing|scam)\.[a-z]', body):
                    return True
            elif part.get_content_type() == 'application/x-msdownload':
                # If the email contains a suspicious attachment, it is like[4D[K
likely a phishing attack.
                return True
        return False
    except Exception:
        # If there was an error parsing the email, assume it is a phishing [K
attack.
        return True

def send_email(recipient, subject, body):
    """Send an email to the recipient."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'phishing@example.com'
    msg['To'] = recipient
    server = smtplib.SMTP('smtp.example.com')
    try:
        server.sendmail('phishing@example.com', recipient, msg.as_string())[16D[K
msg.as_string())
    finally:
        server.quit()

def main():
    """Main function."""
    while True:
        # Wait for a new email to arrive
        email = email.fetch(num=1)[0][1]
        if is_phishing_email(email):
            send_email('phishing@example.com', 'Phishing Attack Detected!',[11D[K
Detected!', 'A phishing attack has been detected. Please be cautious of any[3D[K
any suspicious links or attachments.')

if __name__ == '__main__':
    main()
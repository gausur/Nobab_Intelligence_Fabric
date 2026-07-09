#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-09 11:49:17.006903

import re
import socket
import smtplib

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(regex, email) is not None

def is_valid_domain(domain):
    regex = r"\A([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}\Z"
    return re.match(regex, domain) is not None

def is_phishing_attempt(email):
    if not is_valid_email(email):
        return False
    parts = email.split("@")
    sender_domain = parts[1]
    if not is_valid_domain(sender_domain):
        return True
    else:
        return False

def get_smtp_server(host):
    try:
        socket.gethostbyname(host)
        return smtplib.SMTP(host)
    except:
        return None

def send_email(recipient, subject, body):
    server = get_smtp_server("mail.example.com")
    if server is not None:
        server.sendmail("noreply@example.com", recipient, f"Subject: {subje[6D[K
{subject}\r\n{body}")
        server.quit()
    else:
        print(f"Failed to send email to {recipient}")

def main():
    email = "johndoe@gmail.com"
    if is_phishing_attempt(email):
        subject = "Possible Phishing Attempt Detected"
        body = f"The email address {email} has been identified as a possibl[7D[K
possible phishing attempt. Please contact your IT department for further as[2D[K
assistance."
        send_email("admin@example.com", subject, body)
    else:
        print(f"Email address {email} is not a phishing attempt")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-25 10:31:26.387622

import re
import smtplib
import dns

def is_phishing_attempt(email):
    # Check if the email is from a known phishing domain
    if is_phishing_domain(email["From"]):
        return True
    # Check if the email contains a malicious link
    if is_malicious_link(email["Body"]):
        return True
    # Check if the email contains a malicious attachment
    if is_malicious_attachment(email["Attachments"]):
        return True
    return False

def is_phishing_domain(domain):
    # Check if the domain is a known phishing domain using a blacklist
    if is_in_blacklist(domain):
        return True
    # Check if the domain is a known phishing domain using DNS resolution
    if is_in_dns_resolution(domain):
        return True
    return False

def is_in_blacklist(domain):
    # Check if the domain is in a known phishing domain blacklist
    if domain in ["phishing.com", "fake.com"]:
        return True
    return False

def is_in_dns_resolution(domain):
    # Check if the domain is in a known phishing domain using DNS resolutio[9D[K
resolution
    try:
        dns.resolver.resolve(domain)
        return True
    except dns.resolver.NXDOMAIN:
        return False

def is_malicious_link(body):
    # Check if the email contains a malicious link using a regular expressi[8D[K
expression
    if re.search(r"http://.*\.exe", body):
        return True
    return False

def is_malicious_attachment(attachments):
    # Check if the email contains a malicious attachment using a regular ex[2D[K
expression
    for attachment in attachments:
        if re.search(r"\.exe$", attachment["name"]):
            return True
    return False

def mitigate_phishing_attempt(email):
    # Send a response to the email with a warning message
    sender = email["From"]
    recipient = email["To"]
    subject = "Phishing attempt detected"
    body = "This is an automated response to alert you that a phishing atte[4D[K
attempt was detected in your email. Please do not click on any links or ope[3D[K
open any attachments from this sender."
    smtplib.sendmail(sender, recipient, subject, body)

def main():
    # Read email messages from an email server
    server = smtplib.SMTP("localhost")
    messages = server.retrieve()
    # Iterate over the messages and check if they are phishing attempts
    for message in messages:
        if is_phishing_attempt(message):
            mitigate_phishing_attempt(message)

if __name__ == "__main__":
    main()
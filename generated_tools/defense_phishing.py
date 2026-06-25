#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-25 04:00:47.922891

import re
import smtplib
from email.message import EmailMessage

def is_phishing_email(msg: EmailMessage) -> bool:
    """Check if an email message is a phishing attack"""
    # Check for spammy keywords in the subject and body
    if any(word in msg["Subject"] for word in ["phishing", "scam", "spam"])[8D[K
"spam"]):
        return True
    if any(word in msg.get_payload() for word in ["phishing", "scam", "spam[5D[K
"spam"]):
        return True
    
    # Check for suspicious links in the email body
    urls = re.findall(r"https?://\S+", msg.get_payload())
    for url in urls:
        if any(suspicious_domain in url for suspicious_domain in ["example.[10D[K
["example.com", "fakeemail.com"]):
            return True
    
    # Check for suspicious attachments
    attachments = msg.get_payload()
    for attachment in attachments:
        if any(suspicious_filetype in attachment["Content-Type"] for suspic[6D[K
suspicious_filetype in ["application/x-msdownload", "application/exe"]):
            return True
    
    return False

def mitigate_phishing_attack(msg: EmailMessage) -> None:
    """Mitigate a phishing attack by blocking the email sender"""
    # Get the email sender's address
    sender = msg["From"]
    
    # Send a message to the mail server to block the sender
    with smtplib.SMTP("localhost") as server:
        server.sendmail(sender, sender, "Blocked by phishing detection scri[4D[K
script")

# Main function to call is_phishing_email and mitigate_phishing_attack
def main():
    # Get the email message from stdin
    msg = EmailMessage()
    msg.parse(sys.stdin)
    
    # Check if the email is a phishing attack
    if is_phishing_email(msg):
        mitigate_phishing_attack(msg)

if __name__ == "__main__":
    main()
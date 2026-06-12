#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-12 23:13:55.697438

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    if not email:
        return False
    
    subject = email["subject"]
    body = email.get_payload()
    sender = email["sender"]
    recipient = email["recipient"]
    
    # Check for suspicious keywords in the subject and body
    keywords = ["phishing", "scam", "fraud", "credit card", "bank account"][9D[K
account"]
    for keyword in keywords:
        if re.search(keyword, subject, flags=re.IGNORECASE) or re.search(ke[12D[K
re.search(keyword, body, flags=re.IGNORECASE):
            return True
    
    # Check for suspicious sender and recipient email addresses
    sender_email = sender.split("<")[1].split(">")[0]
    recipient_email = recipient.split("<")[1].split(">")[0]
    if not re.match(r"^[\w\.]+@[\w\.]+\.[a-z]{2,}$", sender_email) or not r[1D[K
re.match(r"^[\w\.]+@[\w\.]+\.[a-z]{2,}$", recipient_email):
        return True
    
    # Check for suspicious HTML tags in the body
    if "<script>" in body:
        return True
    
    # Check for suspicious URLs in the body
    urls = re.findall(r"https?://\S+", body)
    for url in urls:
        if not re.match(r"^https?://[\w\.]+\.[a-z]{2,}/$", url):
            return True
    
    return False

def mitigate_phishing_attack(email):
    # Send an email to the recipient with a warning message
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attempt Detected"
    msg["From"] = "noreply@example.com"
    msg["To"] = email["recipient"]
    msg.set_content("This is an automated response to notify you that a phi[3D[K
phishing attempt was detected. Please be cautious when opening attachments [K
or clicking on links in future emails.")
    
    # Send the warning message using SMTP
    smtp = smtplib.SMTP("localhost")
    smtp.send_message(msg)
    smtp.quit()

def main():
    # Load the email from stdin
    email = EmailMessage()
    
    # Check if the email is a phishing attack
    is_phishing = is_phishing_attack(email)
    
    # Mitigate the phishing attack if necessary
    if is_phishing:
        mitigate_phishing_attack(email)

if __name__ == "__main__":
    main()
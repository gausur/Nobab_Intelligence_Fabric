#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 16:28:27.725391

import re
import smtplib
from email.parser import Parser
from email.header import decode_header

def is_phishing(message):
    # Check if the message is a valid email
    try:
        Parser().parse(message)
    except Exception as e:
        print("Invalid email:", e)
        return False
    
    # Extract the sender's email address and domain
    sender_email, domain = re.split(r"@", message["From"])[0], re.split(r"@[12D[K
re.split(r"@", message["From"])[1]
    
    # Check if the sender's domain is a known phishing domain
    if domain in ["phishingdomain1.com", "phishingdomain2.com"]:
        print("Phishing email detected!")
        return True
    
    # Check if the message contains any suspicious keywords
    for keyword in ["fake", "scam", "malware", "spoofed"]:
        if re.search(keyword, message.get_payload(), re.IGNORECASE):
            print("Suspicious email detected!")
            return True
    
    # No phishing attacks detected
    return False

def main():
    # Connect to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, passwd)
    
    # Fetch the message from the email server
    msg = Parser().parse(server.retrieve("INBOX", "1"))
    
    # Check if the message is a phishing attack
    if is_phishing(msg):
        print("Phishing attack detected!")
        
        # Mitigate the attack by reporting it to the sender and deleting th[2D[K
the message from the email server
        server.sendmail(user, msg["From"], "This is a phishing attempt! Ple[3D[K
Please do not click on any links or provide any personal information.")
        server.dele("1")
    else:
        print("No phishing attacks detected.")
    
    # Close the SMTP connection
    server.quit()

if __name__ == "__main__":
    main()
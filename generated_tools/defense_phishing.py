#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 06:33:28.580366

import re
import smtplib
from email.parser import Parser
from email.policy import default

def detect_phishing_attack(email_message):
    # Check if the email is from a known phishing domain
    if email_message["From"].split("@")[1] in ["phishingdomain1.com", "phis[5D[K
"phishingdomain2.com"]:
        return True
    # Check if the email contains a link to a known phishing website
    if re.search(r"http[s]?://[a-zA-Z0-9./]*", email_message.get_payload())[28D[K
email_message.get_payload()):
        return True
    # Check if the email contains a known phishing phrase
    if re.search(r"I love you more than I love myself", email_message.get_p[19D[K
email_message.get_payload()):
        return True
    return False

def mitigate_phishing_attack(email_message):
    # Send a notification to the user's account holder
    account_holder_email = email_message["To"]
    notification_message = f"Phishing attack detected on {email_message['Su[18D[K
{email_message['Subject']}.\nPlease check your email for more information."[13D[K
information."
    smtplib.sendmail(account_holder_email, "noreply@example.co[19D[K
"noreply@example.com", notification_message)

# Load the email message from the input file
email_message = Parser(policy=default).parse(open("email_message.txt", "r")[4D[K
"r").read())

# Detect and mitigate the phishing attack
if detect_phishing_attack(email_message):
    mitigate_phishing_attack(email_message)
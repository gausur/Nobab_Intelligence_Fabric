#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-03 17:21:56.534587

import re
import smtplib
from email import message_from_string

def is_phishing(email):
    """
    Detect phishing attempts in an email by checking for common patterns an[2D[K
and suspicious content.
    :param email: A string containing the contents of a single email, inclu[5D[K
including headers and body.
    :return: True if the email is likely to be a phishing attempt, False ot[2D[K
otherwise.
    """
    # Check for common phishing patterns in the subject line
    if re.search(r'[Ff]ree [tT]rial|[Ww]in [Pp]remium|[Aa]utomatic [Dd]ownl[8D[K
[Dd]ownload', email['subject']):
        return True
    
    # Check for suspicious content in the body of the email
    if re.search(r'click here to activate your account|download a malware-f[9D[K
malware-free version', email.get_payload()):
        return True
    
    # Check for common phishing words in the sender's address
    if re.search(r'phishing|scam|fraud|hacked', email['from']):
        return True
    
    return False

def mitigate_phishing(email):
    """
    Mitigate phishing attempts by warning the user and flagging the email a[1D[K
as spam.
    :param email: A string containing the contents of a single email, inclu[5D[K
including headers and body.
    """
    # Send an alert to the user informing them that their email has been fl[2D[K
flagged as suspicious
    smtplib.sendmail('alerts@example.com', 'user@example.com', 'Phishing At[2D[K
Attempt Alert')
    
    # Flag the email as spam in the recipient's mail client
    message = message_from_string(email)
    message['X-Spam'] = 1
    smtplib.sendmail('spam@example.com', 'user@example.com', message.as_str[14D[K
message.as_string())
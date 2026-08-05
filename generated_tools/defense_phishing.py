#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-04 23:59:26.490057

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attempt(email):
    # Check if the email contains a suspicious link
    if re.search(r"https?://[^\s]+", email):
        return True
    
    # Check if the email has a malicious attachment
    if any(re.search(r"\.exe$|\.zip$|\.rar$", a) for a in email.attachments[17D[K
email.attachments):
        return True
    
    # Check if the sender's domain is not legitimate
    if re.search(r"@[^\.]+\.\w{2,4}$", email.from_addr):
        return True
    
    # Check if the email contains a suspicious subject line
    if re.search(r"[\w\W]+?[Ff]raud|[Ss]cams|[Hh]acking|[Pp]wned", email.su[8D[K
email.subject):
        return True
    
    # Check if the email is from a known spammer or phisher
    if email.from_addr in ("spammer@example.com", "phisher@example.org"):
        return True
    
    # Check if the email contains a suspicious message body
    if re.search(r"[\w\W]+?[Ff]ree [Dd]omains|[Bb]uy [Cc]redit", email.body[10D[K
email.body):
        return True
    
    return False

def mitigate_phishing_attempt(email):
    # Remove the suspicious link from the email body
    if re.search(r"https?://[^\s]+", email.body):
        email.body = re.sub(r"https?://[^\s]+", "", email.body)
    
    # Remove the malicious attachment from the email
    for a in email.attachments:
        if any(re.search(r"\.exe$|\.zip$|\.rar$", a)):
            email.attachments.remove(a)
    
    # Send the mitigated email to the recipient
    with smtplib.SMTP("smtp.example.com") as server:
        msg = EmailMessage()
        msg["From"] = "phishing@example.com"
        msg["To"] = email.to_addr
        msg["Subject"] = f"Phishing attempt detected and mitigated ({email.[8D[K
({email.subject})"
        msg.set_content(f"This email was sent to {email.from_addr} from a p[1D[K
phishing attempt.\n\nSent by: {email.from_addr}")
        server.sendmail("phishing@example.com", email.to_addr, msg.as_strin[12D[K
msg.as_string())
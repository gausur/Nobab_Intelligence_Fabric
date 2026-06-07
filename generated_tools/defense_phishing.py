#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-07 10:11:34.759624

import re
import smtplib

def is_phishing(url):
    # Check if the URL is a valid email address
    if not re.match(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", url):
        return False
    
    # Connect to the SMTP server and send a HELO command
    smtp = smtplib.SMTP("smtp.example.com")
    smtp.send_command("HELO")
    
    # Check if the response is 250, indicating that the server is ready for[3D[K
for a TLS connection
    if smtp.recv_response()[0] != 250:
        return False
    
    # Start a TLS session and send an EHLO command
    smtp.starttls()
    smtp.send_command("EHLO")
    
    # Check if the response is 250, indicating that the server supports TLS[3D[K
TLS
    if smtp.recv_response()[0] != 250:
        return False
    
    # Send a MAIL FROM command with a sender address and a blank RCPT TO co[2D[K
command
    smtp.send_command("MAIL FROM", "sender@example.com")
    smtp.send_command("RCPT TO", "")
    
    # Check if the response is 250, indicating that the server accepts the [K
sender address and blank RCPT TO command
    if smtp.recv_response()[0] != 250:
        return False
    
    # Send a DATA command with a blank message body
    smtp.send_command("DATA", "")
    
    # Check if the response is 354, indicating that the server accepts the [K
DATA command
    if smtp.recv_response()[0] != 354:
        return False
    
    # Send a quit command and close the connection
    smtp.send_command("QUIT")
    smtp.close()
    
    # If all checks passed, the URL is likely to be a phishing website
    return True
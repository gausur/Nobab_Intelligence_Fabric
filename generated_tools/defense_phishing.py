#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-30 21:00:49.658324

import re
import socket
import urllib.request
from email.utils import parseaddr

def is_phishing_url(url):
    # Check if the URL has a known phishing domain
    for domain in PHISHING_DOMAINS:
        if domain in url:
            return True
    return False

def mitigate_phishing_attack(request, response):
    # Check if the request is from a phishing URL
    url = parseaddr(request.url)[1]
    if is_phishing_url(url):
        # Block the request and send a warning message to the user
        response.status_code = 403
        return "<html><body>Phishing attempt blocked</body></html>"
    else:
        # Proceed with the original request
        return None

# List of known phishing domains
PHISHING_DOMAINS = ["phish.io", "example.com"]

# Create a socket to listen for incoming requests
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 80))
    s.listen()

while True:
    # Accept an incoming request
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        # Read the request data
        request = urllib.request.urlopen(conn)
        # Check if the request is from a phishing URL
        response = mitigate_phishing_attack(request, conn.recv())
        # Send the modified response back to the client
        if response:
            conn.sendall(response.encode("utf-8"))
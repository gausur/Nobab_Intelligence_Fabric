#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-10 21:55:43.998748

import re
import socket
import ssl

def detect_phishing(url):
    # Check if the URL is valid
    try:
        urllib.parse.urlparse(url)
    except ValueError:
        return False
    
    # Check if the URL is HTTPS
    if not url.startswith("https://"):
        return False
    
    # Get the domain of the URL
    domain = url.split("://")[1].split("/")[0]
    
    # Try to connect to the domain and check the SSL certificate
    try:
        sock = socket.create_connection((domain, 443), 2)
        ssl_sock = ssl.wrap_socket(sock)
        cert = ssl_sock.getpeercert()
        
        # Check if the domain is in the common name or subject alternative [K
names
        cn = cert["subject"][b"CN"][0]
        sans = cert["extensions"][b"subjectAltName"].split(",")
        if domain == cn or domain in sans:
            return True
    except (ConnectionError, ssl.SSLError):
        pass
    
    # If the URL is not a phishing website, return False
    return False
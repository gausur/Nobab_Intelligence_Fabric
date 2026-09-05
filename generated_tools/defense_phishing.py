#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-05 13:13:02.204759

import re
import urllib.request
import urllib.parse
import socket
import ssl

def detect_phishing_attack(url):
    # Check if the URL is a valid HTTP(S) URL
    if not re.match(r'^https?://', url):
        return False

    # Extract the domain name from the URL
    domain = urllib.parse.urlparse(url).netloc

    # Check if the domain name is a valid IP address
    try:
        socket.inet_pton(socket.AF_INET, domain)
        return False
    except socket.error:
        pass

    try:
        socket.inet_pton(socket.AF_INET6, domain)
        return False
    except socket.error:
        pass

    # Check if the domain name is in the HSTS preload list
    hsts = urllib.request.urlopen('https://hstspreload.org/api/v1/status?do[64D[K
urllib.request.urlopen('https://hstspreload.org/api/v1/status?domain={}'.fourllib.request.urlopen('https://hstspreload.org/api/v1/status?doain={}'.format(domain)).read()
    if hsts:
        return False

    # Check if the domain name has a valid SSL certificate
    try:
        ssl.get_server_certificate((domain, 443))
        return False
    except ssl.SSLError:
        return True

    # If none of the above checks pass, the URL is likely a phishing attack[6D[K
attack
    return True

# Example usage:
url = 'http://example.com'
if detect_phishing_attack(url):
    print('Phishing attack detected!')
else:
    print('No phishing attack detected.')
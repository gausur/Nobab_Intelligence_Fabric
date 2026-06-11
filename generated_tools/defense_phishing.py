#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-11 18:11:23.377137

import re
import socket
from urllib.request import urlopen, URLError

def is_phishing_attack(url):
    try:
        # Fetch the URL and check if it returns a 200 OK status code
        response = urlopen(url)
        return response.getcode() == 200
    except URLError:
        # If the URL cannot be opened, it may be a phishing attack
        return True

def mitigate_phishing_attack(url):
    # Check if the URL is a valid domain name
    if not re.match(r'^https?://\S+', url):
        print("Invalid URL")
        return

    # Fetch the website's SSL/TLS certificate information
    try:
        context = ssl.create_default_context()
        connection = context.wrap_socket(socket.socket(), server_hostname=u[17D[K
server_hostname=url)
        connection.connect((url, 443))
        cert = connection.getpeercert()
    except (URLError, socket.gaierror):
        # If the URL cannot be reached or is not an HTTPS website, skip mit[3D[K
mitigation
        return

    # Check if the certificate is valid and issued by a trusted CA
    if cert['notAfter'] < datetime.datetime.utcnow():
        print("Certificate has expired")
        return

    if 'organizationName' not in cert:
        print("Invalid or missing organization name in certificate")
        return

    # Check if the certificate's issuer is a trusted CA
    if cert['issuer']['organizationalUnitName'] != 'security@example.com':
        print("Certificate is not issued by a trusted CA")
        return

    # If all checks pass, the website is likely legitimate and safe to visi[4D[K
visit
    print("Website appears to be legitimate and safe to visit")

if __name__ == '__main__':
    url = input("Enter URL: ")
    mitigate_phishing_attack(url)
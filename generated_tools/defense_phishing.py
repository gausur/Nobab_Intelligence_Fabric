#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 18:31:27.249261

import re
import socket
import ssl
import urllib.request

def is_phishing(url):
    try:
        # Get the domain of the URL
        domain = urlparse(url).netloc

        # Check if the domain is in the Public Suffix List
        if not tld.contains_suffix(domain):
            return True

        # Check if the URL is using HTTPS
        if urllib.request.urlopen(url, timeout=5).getcode() != 200:
            return True

        # Get the SSL certificate for the domain
        cert = ssl.get_server_certificate((domain, 443))

        # Check if the SSL certificate is valid and issued by a trusted CA
        try:
            x509.load_pem_x509_certificate(str.encode(cert)).check_validity[63D[K
x509.load_pem_x509_certificate(str.encode(cert)).check_validity()
            return False
        except ValueError as e:
            print(e)
            return True
    except (urllib.request.URLError, socket.timeout):
        return True
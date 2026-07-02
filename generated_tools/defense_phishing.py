#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-02 06:34:37.038188

import re
import socket
import ssl

def is_phishing(url):
    if "http" not in url:
        return False
    try:
        sock = socket.socket()
        sock.connect((url, 443))
        ssl_sock = ssl.wrap_socket(sock)
        ssl_sock.do_handshake()
        cert = ssl_sock.getpeercert()
    except:
        return False
    if "CN=*.google.com" in cert["subjectAltName"]:
        return True
    else:
        return False
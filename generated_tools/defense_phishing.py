#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-25 18:31:45.512467

import re
import socket
import ssl

def is_phishing_attack(url):
    """
    Detects a phishing attack by checking the URL for common patterns and
    verifying the SSL certificate.
    """
    # Check for common patterns in the URL
    if re.search(r"^https://www\.phishing\.com/", url):
        return True
    elif re.search(r"^http://www\.phishing\.com/", url):
        return True
    elif re.search(r"^https://phishing\.com/", url):
        return True
    elif re.search(r"^http://phishing\.com/", url):
        return True

    # Verify the SSL certificate
    try:
        context = ssl.create_default_context()
        socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.S[8D[K
socket.SOCK_STREAM))
        socket.connect((url, 443))
        ssl_connection = context.wrap_socket(socket, server_hostname=url)
        ssl_connection.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        response = ssl_connection.recv(4096)
        ssl_connection.close()
    except:
        return False

    # Check for common SSL errors
    if response.startswith(b"HTTP/1.0 200 OK"):
        return True
    elif response.startswith(b"HTTP/1.0 403 Forbidden"):
        return True
    elif response.startswith(b"HTTP/1.0 404 Not Found"):
        return True
    elif response.startswith(b"HTTP/1.0 405 Method Not Allowed"):
        return True
    elif response.startswith(b"HTTP/1.0 429 Too Many Requests"):
        return True
    else:
        return False

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    if is_phishing_attack(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")
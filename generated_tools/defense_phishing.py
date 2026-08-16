#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-16 21:16:46.895163

import re
import socket

def is_phishing_url(url):
    pattern = r"(https?://)((?:www\.)?(?:[^.]+\.)+(?:com|org|net|edu))"
    if re.match(pattern, url):
        return True
    else:
        return False

def is_phishing_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

def is_phishing_ip(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-[61D[K
r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-][0-9]|[01]?[0-9][0-9]?)$"
    if re.match(pattern, ip):
        return True
    else:
        return False

def mitigate_phishing(url, email, ip):
    if is_phishing_url(url):
        print("Phishing URL detected!")
        return
    elif is_phishing_email(email):
        print("Phishing email detected!")
        return
    elif is_phishing_ip(ip):
        print("Phishing IP detected!")
        return
    else:
        print("No phishing detected!")

url = "https://www.example.com"
email = "example@example.com"
ip = "192.168.0.1"
mitigate_phishing(url, email, ip)
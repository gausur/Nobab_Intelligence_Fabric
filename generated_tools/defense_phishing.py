#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-18 15:47:58.907561

import re
import urllib.parse
from email.message import EmailMessage

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    hostname = parsed_url.hostname
    domain = hostname[hostname.index(".") + 1:]
    if domain in ["google", "gmail"]:
        return True
    return False

def is_phishing_email(email):
    msg = EmailMessage()
    msg.set_content(email)
    for part in msg.iter_parts():
        if part["Content-Type"].startswith("text/html"):
            html = part.get_payload(decode=True).decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            for link in soup.find_all("a", href=True):
                if is_phishing_url(link["href"]):
                    return True
    return False

def mitigate_phishing_attack(email):
    msg = EmailMessage()
    msg.set_content(email)
    for part in msg.iter_parts():
        if part["Content-Type"].startswith("text/html"):
            html = part.get_payload(decode=True).decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            for link in soup.find_all("a", href=True):
                if is_phishing_url(link["href"]):
                    link["href"] = "#"
    return msg.as_string()
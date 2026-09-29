#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-29 19:05:19.366490

import re
import requests
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme != "https":
        return True
    if parsed_url.netloc.endswith(".onion"):
        return True
    if parsed_url.netloc.endswith(".pw"):
        return True
    if parsed_url.netloc.endswith(".cf"):
        return True
    if parsed_url.netloc.endswith(".in"):
        return True
    if parsed_url.netloc.endswith(".com.cn"):
        return True
    if parsed_url.netloc.endswith(".com.au"):
        return True
    if parsed_url.netloc.endswith(".com.tw"):
        return True
    if parsed_url.netloc.endswith(".com.hk"):
        return True
    if parsed_url.netloc.endswith(".com.tw"):
        return True
    if parsed_url.netloc.endswith(".com.vn"):
        return True
    return False

def is_phishing_email(email):
    if "@" in email:
        local, domain = email.split("@")
        if local.isdigit() or domain.isdigit():
            return True
    return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        return url.replace("https://", "").replace("http://", "")
    return url

def main():
    url = input("Enter the URL: ")
    if is_phishing_url(url):
        print("The URL is a phishing attack!")
        mitigate_phishing_attack(url)
    else:
        print("The URL is not a phishing attack!")

if __name__ == "__main__":
    main()
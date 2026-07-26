#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-26 23:56:31.626281

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    """
    Detects whether a URL is a phishing site by analyzing its DNS, HTTP hea[3D[K
headers, and HTML content.
    """
    parsed = urlparse(url)
    hostname = parsed.hostname
    dns_records = requests.get('https://api.hackertarget.com/hostsearch/?q=[57D[K
requests.get('https://api.hackertarget.com/hostsearch/?q=%s' % hostname).te[12D[K
hostname).text.split('\n')
    for line in dns_records:
        if re.match(r'\d+\.\d+\.\d+\.\d+', line):
            ip = line.strip()
            if not is_valid_ip(ip):
                return True
            else:
                return False
    http_headers = requests.get('https://api.hackertarget.com/httpheaders/?[56D[K
requests.get('https://api.hackertarget.com/httpheaders/?q=%s' % url).text.s[11D[K
url).text.split('\n')
    for line in http_headers:
        if re.match(r'Set-Cookie:\s+', line):
            cookie = line.strip()[10:]
            if not is_valid_cookie(cookie):
                return True
            else:
                return False
    html_content = requests.get(url).text
    for line in html_content.split('\n'):
        if re.match(r'<script>', line):
            script = line[7:]
            if not is_valid_script(script):
                return True
            else:
                return False
    return False

def is_valid_ip(ip):
    """
    Checks whether an IP address is valid by analyzing its format.
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        return True
    else:
        return False

def is_valid_cookie(cookie):
    """
    Checks whether a cookie is valid by analyzing its format.
    """
    pattern = r'^[^=]+=[^;]*$'
    if re.match(pattern, cookie):
        return True
    else:
        return False

def is_valid_script(script):
    """
    Checks whether a script is valid by analyzing its format.
    """
    pattern = r'^<\w+\s+[^>]*>.*</\w+>'
    if re.match(pattern, script):
        return True
    else:
        return False

if __name__ == '__main__':
    url = input('Enter the URL to check for phishing attacks: ')
    if is_phishing(url):
        print('The URL is a phishing site!')
    else:
        print('The URL is not a phishing site.')
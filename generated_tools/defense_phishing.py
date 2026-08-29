#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-29 23:46:34.566529

import re
import urllib.request
import urllib.error
import socket

def detect_phishing(url):
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozil[6D[K
'Mozilla/5.0'})
        response = urllib.request.urlopen(request)
        data = response.read()
    except (urllib.error.URLError, socket.error):
        return False

    # Check for suspicious keywords in the page source
    for keyword in ['phishing', 'scam', 'fraud', 'malware']:
        if keyword in data.decode('utf-8'):
            return False

    # Check for suspicious HTTP headers
    headers = response.info()
    for header in ['Set-Cookie', 'Location', 'Refresh']:
        if header in headers:
            return False

    return True

def main():
    url = input('Enter the URL: ')
    if detect_phishing(url):
        print('The URL is safe.')
    else:
        print('The URL is not safe.')

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-21 23:53:48.276626

import re
from urllib import request

def is_phishing(url):
    if not re.match(r'^https?://', url):
        return False
    try:
        response = request.urlopen(url)
        html = response.read().decode('utf-8')
        if '</title>' in html and 'phishing' in html.lower():
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Detected phishing attack. Blocking...")
        return
    else:
        print("No phishing attack detected.")
        return

if __name__ == '__main__':
    url = input("Enter URL to check for phishing attacks: ")
    mitigate_phishing(url)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 11:49:55.792543

import re
import requests
from urllib import parse

def is_phishing(url):
    if not re.match(r'^https?://', url):
        return False
    try:
        response = requests.get(url)
        html = response.text
        title = re.search(r'<title>(.*?)</title>', html)
        if title is None or not title.group(1).lower().startswith('phishing[43D[K
title.group(1).lower().startswith('phishing'):
            return False
    except requests.exceptions.RequestException:
        pass
    return True

def mitigate_phishing(url):
    parsed = parse.urlparse(url)
    if is_phishing(parsed.netloc + '://' + parsed.path):
        print('Phishing attempt detected!')
        print('Please report this incident to your IT department.')
    else:
        print('No phishing attempt detected.')
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-01 09:55:43.802399

import re
import sys
import urllib

def is_phishing(url):
    pattern = r'https?://[a-zA-Z0-9.-]+(:[0-9]+)?/\S+'
    if not re.match(pattern, url):
        return False
    try:
        host = urllib.parse.urlsplit(url).hostname
        if host in ['gmail.com', 'yahoo.com', 'hotmail.com']:
            return True
        else:
            return False
    except ValueError:
        return False

def mitigate_phishing(url):
    try:
        urllib.parse.quote(url, safe='')
    except ValueError:
        sys.stderr.write('Invalid URL\n')
        exit(1)
    if is_phishing(url):
        print('Phishing attack detected! Please report this incident to the[3D[K
the appropriate authorities.')
    else:
        print('No phishing attacks detected.')
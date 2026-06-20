#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 15:33:44.299558

import re
import socket

def detect_phishing(url):
    # Check if the URL is valid
    try:
        socket.gethostbyname(url)
    except:
        return False

    # Check for common phishing URLs
    if re.search(r'https?://(www.)?google\.(com|co\.uk)/', url):
        return False
    elif re.search(r'https?://(www.)?facebook\.(com|co\.uk)/', url):
        return False
    elif re.search(r'https?://(www.)?twitter\.(com|co\.uk)/', url):
        return False
    elif re.search(r'https?://(www.)?linkedin\.(com|co\.uk)/', url):
        return False
    elif re.search(r'https?://(www.)?youtube\.(com|co\.uk)/', url):
        return False

    # Check for common phishing domain names
    if re.search(r'\.(info|co\.uk|net)$', url):
        return True

    # Check for common phishing parameters
    if re.search(r'https?://(www.)?([\w-]+\.)+([\w]+)/[?&]', url):
        return True

    # Check for common phishing path patterns
    if re.search(r'/(login|signin|signup|register|admin|account)\b', url):
        return True

    return False
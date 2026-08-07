#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-07 12:44:32.772089

import re
import ssl
from urllib.parse import urlparse

def is_phishing_url(url):
    # Check if the URL contains any suspicious characters
    if re.search("[^-a-zA-Z0-9.]", url):
        return True
    
    # Check if the URL is for a known phishing website
    parsed_url = urlparse(url)
    if parsed_url.netloc in ["phishingwebsite1.com", "phishingwebsite2.com"[22D[K
"phishingwebsite2.com"]:
        return True
    
    # Check if the URL has a suspicious SSL certificate
    try:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        conn = http.client.HTTPSConnection(parsed_url.netloc, context=ssl_c[13D[K
context=ssl_context)
        conn.request("HEAD", parsed_url.path)
        response = conn.getresponse()
        if response.status == 200:
            return True
    except ssl.SSLError:
        # SSL handshake failed, likely due to a man-in-the-middle attack
        return True
    
    return False
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-12 14:17:55.589512

import re
import ssl
from urllib import request

def is_phishing_site(url):
    # Check if the URL starts with "http" or "https"
    if not (url.startswith("http") or url.startswith("https")):
        return False
    
    # Get the domain name of the URL
    domain = re.search(r'^(?:https?:\/\/)?([^\/]+)(?:\/|$)', url).group(1)
    
    # Check if the domain is in the list of known phishing sites
    with open("phishing_sites.txt", "r") as f:
        for line in f:
            if line.strip() == domain:
                return True
    
    # If the domain is not in the list, check if it has an SSL certificate
    try:
        response = request.urlopen(url)
        if response.code == 200 and ssl.get_server_certificate(response):
            return False
    except Exception as e:
        print(e)
    
    # If the domain has an SSL certificate, check if it is valid
    try:
        cert = ssl.get_server_certificate((domain, 443))
        if cert and ssl.cert_time_to_expire(cert):
            return True
    except Exception as e:
        print(e)
    
    # If the domain has a valid SSL certificate, it is not a phishing site
    return False
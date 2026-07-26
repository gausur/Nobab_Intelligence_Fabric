#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-26 15:00:03.149105

import re
import ssl
from urllib.request import urlopen, Request

def is_phishing(url):
    """
    Check if the given URL is a phishing website using SSL certificate chec[4D[K
checks and DNS information.
    :param url: The URL to check
    :return: True if the URL is a phishing website, False otherwise
    """
    try:
        request = Request(url)
        response = urlopen(request)
        dns_info = response.getheader('DNS-INFO')
        ssl_cert = response.getheader('SSL-CERTIFICATE')
        if not dns_info or not ssl_cert:
            return False
        dns_domain = dns_info.split(' ')[0]
        ssl_issuer = ssl_cert['Issuer']
        if dns_domain != ssl_issuer:
            return True
    except Exception as e:
        print(f'Error detecting phishing website: {e}')
        return False
    return False
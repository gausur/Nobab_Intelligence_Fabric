#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-02 15:00:21.642227

import re
import socket
import dns.resolver
from urllib.parse import urlparse

def is_phishing(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    parsed_url = urlparse(url)
    if not (parsed_url.scheme == "http" or parsed_url.scheme == "https"):
        return False
    
    # Check if the domain name in the URL is a subdomain of the current web[3D[K
website
    hostname = parsed_url.netloc
    if not hostname:
        return False
    if not hostname.startswith("www."):
        hostname = "www." + hostname
    if not hostname.endswith(".com"):
        hostname += ".com"
    current_hostname = socket.gethostname()
    if not current_hostname:
        return False
    if not current_hostname.endswith(".com"):
        current_hostname += ".com"
    if not current_hostname.startswith("www."):
        current_hostname = "www." + current_hostname
    if hostname.find(current_hostname) == -1:
        return False
    
    # Check if the URL is a suspicious domain or IP address
    try:
        resolver = dns.resolver.Resolver()
        answer = resolver.query(hostname, "A")
        for rdata in answer:
            ip_address = str(rdata)
            if not ip_address.startswith("192."):
                return True
    except Exception as e:
        # If the DNS query fails, assume it's a phishing URL
        return True
    
    # Check if the URL is a suspicious path or query
    if parsed_url.path != "/" and not parsed_url.path.startswith("/login") [K
and not parsed_url.path.endswith(".js") and not parsed_url.path.endswith(".[27D[K
parsed_url.path.endswith(".css"):
        return True
    for key, value in parsed_url.query.items():
        if key != "username" and key != "password" and not value.startswith[16D[K
value.startswith("192."):
            return True
    
    # If all checks pass, the URL is likely not a phishing attack
    return False
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-17 21:59:01.097099

import re
import urllib.request
from collections import Counter

def detect_phishing(url):
    # Check if the URL is valid
    if not re.match(r"^https?://", url):
        return "Invalid URL"
    
    # Get the domain of the URL
    domain = urllib.request.urlopen(url).geturl().split("://")[1].split("/"[62D[K
urllib.request.urlopen(url).geturl().split("://")[1].split("/")[0]
    
    # Check if the domain is in the list of known phishing domains
    if domain in PHISHING_DOMAINS:
        return "Phishing attack detected"
    
    # Get the IP address of the URL
    ip = urllib.request.urlopen(url).getheader("X-Forwarded-For")
    
    # Check if the IP is in the list of known phishing IP addresses
    if ip in PHISHING_IPS:
        return "Phishing attack detected"
    
    # Get the user agent of the URL
    ua = urllib.request.urlopen(url).getheader("User-Agent")
    
    # Check if the user agent is in the list of known phishing user agents
    if ua in PHISHING_UAS:
        return "Phishing attack detected"
    
    # Check if the URL contains any suspicious keywords
    if re.search(r"\b(phish|scam|hack)\b", url):
        return "Suspicious keywords detected"
    
    # Check if the URL has a suspicious path
    if re.search(r"/[^/]*\.\./", url):
        return "Suspicious path detected"
    
    # Check if the URL has a suspicious query string
    if re.search(r"[&?]=\w*", url):
        return "Suspicious query string detected"
    
    # Check if the URL has a suspicious fragment
    if re.search(r"\b#\w*", url):
        return "Suspicious fragment detected"
    
    # Check if the URL is from a known malware site
    if urllib.request.urlopen(url).getheader("X-Forwarded-Host") == "malwar[7D[K
"malware":
        return "Malware detected"
    
    return "No phishing attack detected"

# List of known phishing domains
PHISHING_DOMAINS = ["phish.com", "scam.net", "hack.org"]

# List of known phishing IP addresses
PHISHING_IPS = ["192.168.0.1", "10.0.0.1"]

# List of known phishing user agents
PHISHING_UAS = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.[16D[K
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"][15D[K
Safari/537.36"]
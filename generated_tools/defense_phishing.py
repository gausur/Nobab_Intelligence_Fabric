#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-21 20:18:02.280194

import re

def is_phishing_url(url):
    pattern = r"^https?:\/\/(www\.)?(facebook|twitter|linkedin)\.(com|net)\[61D[K
r"^https?:\/\/(www\.)?(facebook|twitter|linkedin)\.(com|net)\/"
    if re.search(pattern, url):
        return False
    else:
        return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

mitigate_phishing_attack("http://www.facebook.com/")
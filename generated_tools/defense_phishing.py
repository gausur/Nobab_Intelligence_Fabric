#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-27 18:51:36.892546

import re

def is_phishing_url(url):
    return re.search(r"(https?:\/\/)?(www\.)?[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3[64D[K
re.search(r"(https?:\/\/)?(www\.)?[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(:[0-9]+)?re.search(r"(https?:\/\/)?(www\.)?[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3(:[0-9]+)?(\/\S*)?", url)

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

mitigate_phishing_attack("https://www.example.com")
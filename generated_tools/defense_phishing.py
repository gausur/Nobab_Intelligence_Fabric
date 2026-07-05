#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-05 20:10:54.118315

import re
from urllib import request
from http.client import HTTPResponse

def is_phishing(url):
    response = request.urlopen(url)
    html = response.read().decode("utf-8")
    return "phishing" in html

def mitigate_phishing(url):
    if is_phishing(url):
        print("Phishing attack detected!")
        return None
    else:
        return url

if __name__ == "__main__":
    url = input("Enter a URL: ")
    mitigated_url = mitigate_phishing(url)
    if mitigated_url is not None:
        print("Mitigated URL:", mitigated_url)
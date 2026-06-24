#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-24 22:11:28.243548

import re
import requests

def detect_phishing(url):
    """
    Detects if the given URL is a phishing site using regular expressions
    :param url: The URL to be checked
    :return: True if it is a phishing site, False otherwise
    """
    regex = r"^(?:(?:https?|ftp):\/\/)?(?:(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z[63D[K
r"^(?:(?:https?|ftp):\/\/)?(?:(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?r"^(?:(?:https?|ftp):\/\/)?(?:(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z-9])?\.)+(?:[a-z]{2,6}\.?|[a-z0-9-]{2,}\.?)|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d{1[a-z]{2,6}\.?|[a-z0-9-]{2,}\.?)|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d{1,5})?(?:\/\S*)?$"
    if re.match(regex, url):
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content
            if b"<title>Login | Phishing Website</title>" in content:
                return True
    return False
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 20:07:52.468934

import re
import requests

def is_phishing_url(url):
    # Check if the URL is valid
    try:
        response = requests.get(url, allow_redirects=False)
    except requests.exceptions.RequestException as e:
        return False

    # Check if the URL is a redirect to another domain
    location = response.headers.get("Location")
    if location and not location.startswith(url):
        return True

    # Check for common phishing patterns in the HTML content
    pattern = r"(?i)(?<=<script>).*?(?=</script>)"
    html_content = response.text
    match = re.search(pattern, html_content)
    if match:
        return True

    # Check for common phishing patterns in the HTTP headers
    pattern = r"x-frame-options:[ ]*deny"
    header = response.headers.get("X-Frame-Options")
    if header and re.match(pattern, header):
        return True

    return False
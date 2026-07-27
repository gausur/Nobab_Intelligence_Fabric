#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-27 20:17:05.564017

import re
from urllib import parse

def detect_phishing(url):
    parsed_url = parse.urlparse(url)
    hostname = parsed_url.hostname
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$[61D[K
r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$"
    if re.search(pattern, hostname):
        return "Phishing attempt detected!"
    else:
        return "No phishing attempt detected."
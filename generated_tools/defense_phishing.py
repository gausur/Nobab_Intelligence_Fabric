#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-29 13:52:25.521409

import re
import sys
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return True
    elif parsed.netloc.endswith("google") or parsed.netloc.endswith("micros[30D[K
parsed.netloc.endswith("microsoft"):
        return False
    else:
        return True

def mitigate_phishing(url):
    if is_phishing(url):
        sys.exit(1)
    else:
        print("Accessing {}".format(url))

mitigate_phishing(sys.argv[1])
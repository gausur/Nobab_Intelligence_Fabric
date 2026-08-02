#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-02 19:01:34.393019

import re
from urllib.parse import urlparse
from email.message import EmailMessage

def is_phishing_url(url):
    parsed = urlparse(url)
    return parsed.hostname and not parsed.hostname.endswith(("gmail.com", "[1D[K
"google.com"))

def is_phishing_email(msg):
    return msg["from"] and msg["from"].lower() == "noreply@example.com" and[3D[K
and any(x in msg["to"] for x in ("yours", "customers", "clients"))

def mitigate_phishing_attacks(msgs, outfile):
    with open(outfile, "w") as f:
        for msg in msgs:
            if is_phishing_url(msg["urls"][0]):
                f.write(f"{msg['from']}: {msg['text']}")

def main():
    with open("infile", "r") as f:
        emails = [EmailMessage().parse(x) for x in f]

    mitigate_phishing_attacks(emails, "outfile")

if __name__ == "__main__":
    main()
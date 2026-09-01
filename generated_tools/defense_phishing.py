#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-01 05:56:04.404347

import re
import socket

class PhishingDetector:
    def __init__(self, hostname):
        self.hostname = hostname
        self.email_re = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-[51D[K
re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        self.url_re = re.compile(r"^(?:http|https)://[a-zA-Z0-9.-]+(:[0-9]+[53D[K
re.compile(r"^(?:http|https)://[a-zA-Z0-9.-]+(:[0-9]+)?/?$")

    def detect_phishing(self, email, url):
        if not self.email_re.match(email):
            raise ValueError("Invalid email")
        if not self.url_re.match(url):
            raise ValueError("Invalid URL")
        return socket.gethostbyname(url) == self.hostname

def main():
    phishing_detector = PhishingDetector("example.com")
    print(phishing_detector.detect_phishing("john.doe@example.com", "https:[7D[K
"https://example.com"))

if __name__ == "__main__":
    main()
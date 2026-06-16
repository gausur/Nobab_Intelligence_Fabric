#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-16 20:43:47.260786

import re
from urllib.parse import urlparse
from html.parser import HTMLParser

class PhishingDetector(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href" and not urlparse(value).netloc:
                    self.mitigate_phishing(value)

    def mitigate_phishing(self, url):
        print("Possible phishing attack detected:", url)

def detect_phishing(html):
    detector = PhishingDetector()
    detector.feed(html)

if __name__ == "__main__":
    with open("index.html") as f:
        html = f.read()
    detect_phishing(html)
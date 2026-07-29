#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-29 05:16:47.111339

import re
import urllib.request
from html.parser import HTMLParser

class PhishingDetector(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.target_domain = urllib.request.urlopen(url).getheader('host')
        self.phish_detected = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for key, value in attrs:
                if key == 'href' and not re.match(r'^https?://' + self.targ[9D[K
self.target_domain + '/', value):
                    self.phish_detected = True

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if not self.phish_detected:
            if re.search(r'^https?://' + self.target_domain + '/', data):
                self.phish_detected = True

    def error(self, message):
        pass

def detect_phishing(url):
    detector = PhishingDetector(url)
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        detector.feed(html)
    return detector.phish_detected

def main():
    url = input("Enter a URL: ")
    if detect_phishing(url):
        print("Possible phishing attack detected!")
    else:
        print("No phishing attacks detected.")

if __name__ == "__main__":
    main()
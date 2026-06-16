#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-16 12:09:22.927599

import re
import urllib.request
from html.parser import HTMLParser

class PhishingDetector(HTMLParser):
    def __init__(self, url):
        self.url = url
        self.links = []
        self.phishing_domains = []
        super().__init__()
    
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and re.match("http://", attr[1]) and r[1D[K
re.match("\w+.\w+", attr[1]):
                    self.links.append(attr[1])
        elif tag == "script":
            for attr in attrs:
                if attr[0] == "src" and re.match("http://", attr[1]):
                    self.phishing_domains.append(attr[1])
    
    def handle_endtag(self, tag):
        pass
    
    def handle_data(self, data):
        if re.search("(?i)phish|scam", data):
            print("Phishing attempt detected!")
            for link in self.links:
                try:
                    urllib.request.urlopen(link)
                except urllib.error.URLError:
                    print("Invalid URL:", link)
    
    def handle_comment(self, data):
        if re.search("(?i)phish|scam", data):
            print("Phishing attempt detected!")
            for domain in self.phishing_domains:
                try:
                    urllib.request.urlopen(domain)
                except urllib.error.URLError:
                    print("Invalid URL:", domain)
    
    def close(self):
        pass

def main():
    detector = PhishingDetector("http://www.example.com")
    detector.feed()

if __name__ == "__main__":
    main()
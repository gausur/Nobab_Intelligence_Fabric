#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-21 19:19:14.789952

import re
import urllib.parse
from email import message_from_bytes
from html.parser import HTMLParser

class PhishingDetector(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.url = None
        self.redirect_url = None
        self.is_phishing = False
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href' and re.match(r'^https?://', value):
                    self.url = value
    
    def handle_endtag(self, tag):
        if tag == 'a':
            self.redirect_url = urllib.parse.urljoin(self.url, self.get_tex[12D[K
self.get_text())
    
    def get_text(self):
        return ''.join(self.text)
    
    def is_phishing_url(self, phishing_domains):
        for domain in phishing_domains:
            if self.redirect_url.startswith(domain):
                self.is_phishing = True
                return True
        return False
    
    def detect_phishing(self, phishing_domains):
        self.feed(self.text)
        self.is_phishing = self.is_phishing_url(phishing_domains)
        return self.is_phishing
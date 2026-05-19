#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-19 20:30:53.265240

import re
import requests
from urllib import parse
from bs4 import BeautifulSoup

def is_phishing(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('input', {'type': 'password'}) is not None:
                return True
    except:
        pass
    return False

def mitigate_phishing(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            for link in soup.find_all('a'):
                if link.get('href').startswith('/'):
                    link['href'] = parse.urljoin(url, link['href'])
            for form in soup.find_all('form'):
                action = form.get('action')
                if action is not None:
                    form['action'] = parse.urljoin(url, action)
            for script in soup.find_all('script'):
                script.extract()
            return soup.prettify(formatter=None)
        else:
            raise ValueError('Invalid URL')
    except:
        pass
    return None

if __name__ == '__main__':
    url = input('Enter URL to check for phishing: ')
    if is_phishing(url):
        print('This website may be a phishing site.')
    else:
        print('This website does not appear to be a phishing site.')
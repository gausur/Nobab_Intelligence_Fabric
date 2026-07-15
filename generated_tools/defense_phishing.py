#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-15 07:11:04.940932

import re
from urllib.parse import urlparse
from email.utils import parseaddr
from typing import List, Tuple, Union

def is_phishing(url: str) -> bool:
    """
    Check if the given URL is a phishing site.
    Return True if the URL is a phishing site, False otherwise.
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    tld = domain_parts[-1]
    if not re.match(r'^[a-zA-Z]{2,}$', tld):
        return False
    for part in domain_parts[:-1]:
        if not re.match(r'^([a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-zA-Z]{2,}[60D[K
re.match(r'^([a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-zA-Z]{2,}$', part):
            return False
    return True

def is_phishing_email(addr: str) -> bool:
    """
    Check if the given email address is a phishing email.
    Return True if the email address is a phishing email, False otherwise.
    """
    try:
        display_name, addr = parseaddr(addr)
    except ValueError:
        return False
    domain = addr.split('@')[1]
    return is_phishing(domain)

def mitigate_phishing(url: str) -> Tuple[str, List[Tuple[int, int]]]:
    """
    Mitigate phishing attacks by removing suspicious parts of the URL.
    Return a tuple containing the modified URL and a list of ranges to be r[1D[K
replaced.
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    scheme = parsed_url.scheme
    if not is_phishing(domain):
        return (url, [])
    modified_url = f'{scheme}://example.com/{parsed_url.path}'
    ranges = [(parsed_url.port, domain)]
    return (modified_url, ranges)

def mitigate_phishing_email(addr: str) -> Union[Tuple[str, List[Tuple[int, [K
int]]], bool]:
    """
    Mitigate phishing attacks by removing suspicious parts of the email add[3D[K
address.
    Return a tuple containing the modified email address and a list of rang[4D[K
ranges to be replaced, or False if the email address is not valid.
    """
    try:
        display_name, addr = parseaddr(addr)
    except ValueError:
        return False
    domain = addr.split('@')[1]
    if not is_phishing(domain):
        return (addr, [])
    modified_addr = f'{display_name} <example@{domain}>'
    ranges = [(addr.find('@') + 1, domain)]
    return (modified_addr, ranges)
#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-29 20:17:26.484076

import re

def is_phishing(url):
    # Check if the URL contains any suspicious patterns
    pattern = r"^(?:ht|f)tp?://|[^/]*\.[a-zA-Z]{2,}$"
    if re.match(pattern, url):
        return False
    
    # Check if the URL is a known phishing site
    blacklist = ["phishng.com", "phishmails.com"]
    if any(blacklisted in url for blacklisted in blacklist):
        return True
    
    # Check if the URL contains any suspicious keywords
    keywords = ["free", "discount", "coupon", "voucher", "promo", "gift"]
    if any(keyword in url for keyword in keywords):
        return True
    
    # If none of the above conditions are met, assume it's not a phishing s[1D[K
site
    return False
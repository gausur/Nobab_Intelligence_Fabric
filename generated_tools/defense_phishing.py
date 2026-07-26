#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-26 05:27:55.176700

import re
import sys

def is_phishing_attack(url):
    pattern = r"(https?:\/\/|www\.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6[61D[K
r"(https?:\/\/|www\.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-r"(https?:\/\/|www\.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_attack(url):
        print("Possible phishing attack detected!")
        sys.exit(1)
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    mitigate_phishing_attack(sys.argv[1])
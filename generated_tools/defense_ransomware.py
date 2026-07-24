#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-24 14:51:23.546354

import os
import re

def is_ransomware(file):
    with open(file, "rb") as f:
        data = f.read()
    return b"RANSOMWARE_KEY" in data or b"Encrypted" in data

def mitigate(file):
    if is_ransomware(file):
        os.remove(file)
        print("Ransomware detected and removed.")
    else:
        print("No ransomware detected.")

if __name__ == "__main__":
    files = os.listdir(".")
    for file in files:
        mitigate(file)
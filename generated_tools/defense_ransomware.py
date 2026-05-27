#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-27 02:39:34.437808

import os
import sys
import time

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if "." not in file:
            continue
        ext = file.split(".")[-1]
        if ext == "exe" or ext == "com":
            print("Possible ransomware detected!")
            return True
    return False

def mitigate_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if "." not in file:
            continue
        ext = file.split(".")[-1]
        if ext == "exe" or ext == "com":
            print("Removing malicious executable!")
            os.remove(os.path.join(path, file))
    return True

if __name__ == "__main__":
    path = sys.argv[1]
    if detect_ransomware(path):
        mitigate_ransomware(path)
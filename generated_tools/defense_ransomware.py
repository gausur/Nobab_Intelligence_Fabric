#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-09-12 17:34:55.497267

import os
import sys

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".enc"):
            return True
    return False

def mitigate_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".enc"):
            os.remove(file)
    return True

def main(args):
    if len(args) != 2:
        print("Usage: python ransomware_detector.py [path]")
        sys.exit(1)

    path = args[1]
    if detect_ransomware(path):
        print("Ransomware detected in path:", path)
        mitigate_ransomware(path)
    else:
        print("No ransomware detected in path:", path)
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
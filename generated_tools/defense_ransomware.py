#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-23 22:56:05.062328

import os
import sys
import shutil

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if "encrypted" in file:
            return True
    return False

def mitigate_ransomware(path):
    if detect_ransomware(path):
        shutil.rmtree(path)
        print("Ransomware detected and mitigated")
        return True
    else:
        print("No ransomware detected")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ransomware_detector.py <path>")
        sys.exit(1)
    path = sys.argv[1]
    mitigate_ransomware(path)
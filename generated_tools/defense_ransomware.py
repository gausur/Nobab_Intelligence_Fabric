#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-25 02:43:24.070108

import os
import sys

def detect_ransomware(file):
    if file.endswith(".exe") or file.endswith(".dll"):
        with open(file, "rb") as f:
            data = f.read()
            for i in range(len(data) - 10):
                if data[i:i+10] == b"RANSOMWARE":
                    return True
    return False

def mitigate_ransomware(file):
    os.remove(file)
    sys.exit()

if __name__ == "__main__":
    for file in os.listdir("."):
        if detect_ransomware(file):
            mitigate_ransomware(file)
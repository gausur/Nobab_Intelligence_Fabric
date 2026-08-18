#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-18 04:31:22.819892

import os
import sys

def detect_ransomware(file):
    with open(file, "rb") as f:
        data = f.read()
        if b"$RANSOM" in data:
            print("Ransomware detected!")
            return True
        else:
            return False

def mitigate_ransomware(file):
    with open(file, "rb") as f:
        data = f.read()
        if b"$RANSOM" in data:
            print("Removing ransomware from file...")
            data = data.replace(b"$RANSOM", b"")
            with open(file, "wb") as f:
                f.write(data)
            print("Ransomware removed!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ransomware_detector.py <file>")
        sys.exit(1)
    file = sys.argv[1]
    if detect_ransomware(file):
        mitigate_ransomware(file)
    else:
        print("No ransomware detected in file.")
#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-21 11:02:55.512705

import os
import sys

def detect_ransomware(filename):
    with open(filename, "rb") as f:
        data = f.read()
        if b"RANSOMWARE" in data:
            print("Detected ransomware!")
            return True
        else:
            print("No ransomware detected.")
            return False

def mitigate_ransomware(filename):
    with open(filename, "rb+") as f:
        data = f.read()
        if b"RANSOMWARE" in data:
            print("Removing ransomware from file...")
            data = data.replace(b"RANSOMWARE", b"")
            f.seek(0)
            f.write(data)
        else:
            print("No ransomware detected.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ransomware_detector.py [filename]")
        sys.exit()
    filename = sys.argv[1]
    detect_ransomware(filename)
    mitigate_ransomware(filename)
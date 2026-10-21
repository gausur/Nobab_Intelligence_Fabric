#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-10-21 22:57:26.206059

import os
import sys

def detect_ransomware(filename):
    with open(filename, "r") as f:
        data = f.read()
        if "demand.txt" in data:
            print("Ransomware detected!")
            return True
        else:
            return False

def mitigate_ransomware(filename):
    with open(filename, "w") as f:
        f.write("")
        print("Ransomware mitigated!")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ransomware_detector.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    if detect_ransomware(filename):
        mitigate_ransomware(filename)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-19 06:33:04.612672

import os
import sys
import json
import subprocess

def detect_ransomware(filename):
    with open(filename, "r") as f:
        data = f.read()
    if "RANSOMWARE" in data:
        return True
    else:
        return False

def mitigate_ransomware(filename):
    with open(filename, "r") as f:
        data = f.read()
    if "RANSOMWARE" in data:
        print("Ransomware detected!")
        subprocess.run(["sudo", "rm", "-rf", filename])
        print("File removed!")
    else:
        print("No ransomware detected.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ransomware_detector.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    if detect_ransomware(filename):
        mitigate_ransomware(filename)
    else:
        print("No ransomware detected.")

if __name__ == "__main__":
    main()
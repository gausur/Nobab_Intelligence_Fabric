#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-23 17:58:55.610602

import os
import sys
import subprocess

def is_ransomware(file):
    return "ransomware" in file.lower()

def detect_ransomware(files):
    for file in files:
        if is_ransomware(file):
            print("Ransomware detected!")
            return True
    return False

def mitigate_ransomware(files):
    for file in files:
        if is_ransomware(file):
            print("Mitigating ransomware...")
            subprocess.run(["rm", "-rf", file])
    return True

def main():
    files = os.listdir()
    if detect_ransomware(files):
        mitigate_ransomware(files)
    else:
        print("No ransomware detected.")

if __name__ == "__main__":
    main()
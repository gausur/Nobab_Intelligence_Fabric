#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-17 05:33:15.339481

import os
import sys

def detect_ransomware(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".exe"):
            with open(file, "r") as f:
                contents = f.read()
                if "Ransomware" in contents:
                    print("Ransomware detected!")
                    return True
    return False

def mitigate_ransomware(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".exe"):
            os.remove(file)

def main():
    directory = sys.argv[1]
    if detect_ransomware(directory):
        mitigate_ransomware(directory)
        print("Ransomware mitigated!")
    else:
        print("No ransomware detected.")

if __name__ == "__main__":
    main()
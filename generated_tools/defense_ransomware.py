#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-24 22:52:06.475729

import os
import sys

def detect_ransomware(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "RANSOMWARE" in open(os.path.join(root, file), "r").read():
                print("Detected ransomware!")
                return True
    return False

def mitigate_ransomware(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "RANSOMWARE" in open(os.path.join(root, file), "r").read():
                print("Removing ransomware from file")
                with open(os.path.join(root, file), "w") as f:
                    f.write("")

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    detected = detect_ransomware(directory)
    if detected:
        mitigate_ransomware(directory)
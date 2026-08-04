#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-04 11:59:34.865335

import os
import shutil
import subprocess
import sys

def detect_ransomware(directory):
    # Check if the directory contains any encrypted files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1] == ".enc":
                return True
    return False

def mitigate_ransomware(directory):
    # Remove the encrypted files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1] == ".enc":
                os.remove(os.path.join(root, file))
    # Delete the directory
    shutil.rmtree(directory)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ransomware_detector.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    if detect_ransomware(directory):
        mitigate_ransomware(directory)
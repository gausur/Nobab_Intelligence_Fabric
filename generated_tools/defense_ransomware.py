#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-04 17:58:59.409860

import os
import time

def detect_ransomware(path):
    files = []
    for root, dirs, _ in os.walk(path):
        for file in dirs:
            if "." in file and file.split(".")[-1] == "tmp":
                files.append(os.path.join(root, file))
    return files

def mitigate_ransomware(files):
    for file in files:
        os.remove(file)

if __name__ == "__main__":
    path = input("Enter the directory to scan: ")
    files = detect_ransomware(path)
    mitigate_ransomware(files)
    print("Ransomware detected and mitigated.")
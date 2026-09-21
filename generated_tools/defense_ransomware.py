#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-09-21 17:32:37.506674

import os
import time

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(file, "r") as f:
                contents = f.read()
                if "Ransomware" in contents:
                    return True
    return False

def mitigate_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(file, "r") as f:
                contents = f.read()
                if "Ransomware" in contents:
                    with open(file, "w") as f:
                        f.write("")

while True:
    path = input("Enter the path to the directory you want to scan: ")
    if detect_ransomware(path):
        mitigate_ransomware(path)
        print("Ransomware detected and mitigated")
    else:
        print("No ransomware detected")
    time.sleep(60)
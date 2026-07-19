#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-19 14:25:01.820950

import os
import sys
import time

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if "." not in file:
            continue
        extension = file[file.index("."):]
        if extension == ".tmp":
            return True
    return False

def mitigate_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if "." not in file:
            continue
        extension = file[file.index("."):]
        if extension == ".tmp":
            os.remove(os.path.join(path, file))

if __name__ == "__main__":
    path = sys.argv[1]
    while True:
        if detect_ransomware(path):
            mitigate_ransomware(path)
            print("Ransomware detected and mitigated.")
            break
        time.sleep(60)
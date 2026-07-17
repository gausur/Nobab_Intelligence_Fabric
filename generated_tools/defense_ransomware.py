#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-17 21:01:23.012582

import os
import shutil

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if not os.path.isfile(os.path.join(path, file)):
            continue
        with open(os.path.join(path, file), "r") as f:
            content = f.read()
            if "RANSOM" in content:
                print("Ransomware detected!")
                return True
    return False

def mitigate_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if not os.path.isfile(os.path.join(path, file)):
            continue
        with open(os.path.join(path, file), "r") as f:
            content = f.read()
            if "RANSOM" in content:
                print("Mitigating ransomware...")
                shutil.move(os.path.join(path, file), "/tmp/")
                break

def main():
    path = "/path/to/your/files"
    if detect_ransomware(path):
        mitigate_ransomware(path)

if __name__ == "__main__":
    main()
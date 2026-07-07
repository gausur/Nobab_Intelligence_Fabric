#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-07 22:08:29.086785

import os
import time

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".exe"):
            with open(os.path.join(path, file), "rb") as f:
                content = f.read()
                if b"RANSOMWARE" in content:
                    return True
    return False

def mitigate_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".exe"):
            with open(os.path.join(path, file), "wb") as f:
                content = b""
                f.write(content)
    return True

def main():
    while True:
        path = input("Enter the path to scan for ransomware: ")
        if detect_ransomware(path):
            mitigate_ransomware(path)
            print("Ransomware detected and mitigated")
        else:
            print("No ransomware detected")
        time.sleep(60)

if __name__ == "__main__":
    main()
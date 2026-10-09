#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-10-09 07:04:06.974442

import os
import shutil

def detect_ransomware(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    if "RANSOMWARE" in f.read():
                        print("Ransomware detected in file:", file)
                        return True
    return False

def mitigate_ransomware(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    if "RANSOMWARE" in f.read():
                        print("Removing ransomware file:", file)
                        os.remove(os.path.join(root, file))
                        return True
    return False

def main():
    directory = os.getcwd()
    if detect_ransomware(directory):
        mitigate_ransomware(directory)

if __name__ == "__main__":
    main()
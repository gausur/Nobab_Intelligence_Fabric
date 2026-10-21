#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-10-21 10:54:43.583386

import os
import json
import shutil
import platform

def detect_ransomware(path):
    if not os.path.exists(path):
        return False
    for file in os.listdir(path):
        if os.path.isfile(file):
            with open(file, "r") as f:
                if "I am a ransomware!" in f.read():
                    return True
    return False

def mitigate_ransomware(path):
    if detect_ransomware(path):
        shutil.rmtree(path)
        return True
    return False

def main():
    if detect_ransomware(os.getcwd()):
        mitigate_ransomware(os.getcwd())
    else:
        print("No ransomware detected")

if __name__ == "__main__":
    main()
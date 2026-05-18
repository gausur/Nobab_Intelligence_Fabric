#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-18 14:36:42.805835

import os
import shutil

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if "ransom" in file.lower():
            return True
    return False

def mitigate_ransomware(path):
    shutil.rmtree(path)

if __name__ == "__main__":
    if detect_ransomware("."):
        mitigate_ransomware(".")
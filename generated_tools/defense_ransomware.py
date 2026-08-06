#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-06 07:40:19.117373

import os
import sys
import subprocess

def check_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if "LOCK" in file:
            return True
    return False

def mitigate_ransomware(path):
    subprocess.call("rm -rf " + path, shell=True)

if __name__ == "__main__":
    path = sys.argv[1]
    if check_ransomware(path):
        mitigate_ransomware(path)
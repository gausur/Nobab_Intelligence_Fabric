#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-15 10:16:52.756531

import os
import re
import shutil

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(".exe"):
            with open(os.path.join(path, file), "r") as f:
                content = f.read()
                if re.search(r"ransom", content):
                    return True
    return False

def mitigate_ransomware(path):
    if detect_ransomware(path):
        shutil.rmtree(path)
        print("Ransomware detected and mitigated.")
    else:
        print("No ransomware detected.")

if __name__ == "__main__":
    mitigate_ransomware(os.getcwd())
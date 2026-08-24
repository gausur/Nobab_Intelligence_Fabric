#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-24 18:30:59.534166

import os
import shutil

def detect_ransomware(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.ransom'):
            return True
    return False

def mitigate_ransomware(path):
    if detect_ransomware(path):
        shutil.rmtree(path)

mitigate_ransomware('/path/to/directory')
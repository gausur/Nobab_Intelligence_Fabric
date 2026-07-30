#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-30 10:18:34.984316

import os
import shutil

def detect_ransomware(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                return True
    return False

def mitigate_ransomware(directory):
    shutil.rmtree(directory)
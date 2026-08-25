#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-25 12:35:00.662717

import os
import shutil

def detect_ransomware(directory):
    for file in os.listdir(directory):
        if not file.endswith(".py"):
            with open(file, "r") as f:
                contents = f.read()
                if "demand" in contents:
                    print(f"Ransomware detected in {file}")
                    shutil.move(file, "ransomware_detected")

detect_ransomware(".")
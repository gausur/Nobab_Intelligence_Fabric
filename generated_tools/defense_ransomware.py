#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-18 17:20:54.294283

import os
import sys
import subprocess

def detect_ransomware():
    try:
        subprocess.check_output(['ls', '-l'])
    except subprocess.CalledProcessError:
        print("Ransomware detected!")
        os.remove('flag.txt')
        sys.exit(1)

if __name__ == '__main__':
    detect_ransomware()
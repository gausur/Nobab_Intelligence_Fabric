#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-23 16:24:27.081547

import os
import time

def detect_ransomware(path):
    for file in os.listdir(path):
        if file.endswith('.docx'):
            with open(file, 'rb') as f:
                data = f.read()
                if b'WannaCry' in data or b'NotPetya' in data:
                    return True
    return False

def mitigate_ransomware(path):
    for file in os.listdir(path):
        if detect_ransomware(file):
            os.remove(file)

if __name__ == '__main__':
    start_time = time.time()
    mitigate_ransomware('path/to/files')
    print("Elapsed time:", time.time() - start_time)
#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-18 11:20:17.548654

import os
import stat
import shutil
import subprocess

def is_executable(path):
    return stat.S_IXUSR & os.stat(path).st_mode

def mitigate_ransomware(path):
    if is_executable(path):
        try:
            subprocess.check_call(['chmod', '-x', path])
        except subprocess.CalledProcessError:
            pass
        shutil.rmtree(path, ignore_errors=True)

def main():
    for root, dirs, files in os.walk('/'):
        for filename in files:
            filepath = os.path.join(root, filename)
            mitigate_ransomware(filepath)

if __name__ == '__main__':
    main()
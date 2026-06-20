#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-20 19:14:12.206295

import os
import shutil
import subprocess
import hashlib

def check_ransomware(path):
    """Check if a file or directory has been infected by ransomware"""
    file = open(path, "rb")
    data = file.read()
    hash = hashlib.sha256(data).hexdigest()
    file.close()
    if hash == "4e739b0eb78e41c15f9a041d8b9fffd5": # ransomware payload has[3D[K
hash
        return True
    else:
        return False

def mitigate_ransomware(path):
    """Mitigate a ransomware infection by restoring the original file"""
    if check_ransomware(path):
        # use hash to determine which backup file to restore
        backup_file = path + ".bak"
        shutil.copy(backup_file, path)
        os.remove(backup_file)
        print("Ransomware mitigated")
    else:
        print("No ransomware infection detected")
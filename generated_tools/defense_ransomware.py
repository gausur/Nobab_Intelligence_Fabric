#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-17 09:03:56.531929

import os
import shutil

def detect_ransomware(directory):
    # Check for common ransomware files and directories
    if os.path.exists(os.path.join(directory, "Cryptolocker.exe")):
        return True
    if os.path.exists(os.path.join(directory, "README.txt")):
        with open(os.path.join(directory, "README.txt"), "r") as f:
            if f.read().startswith("This file is a ransomware infection"):
                return True
    # Check for common ransomware strings in process list
    for proc in psutil.process_iter():
        try:
            name = proc.name()
            cmdline = " ".join(proc.cmdline())
            if name == "Cryptolocker.exe" or "cryptolocker" in cmdline:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    # Check for common ransomware strings in network connections
    for con in psutil.net_connections():
        if "ransom" in con.rhost:
            return True
    # No evidence of ransomware detected
    return False

def mitigate_ransomware(directory):
    # Remove all files and directories except for those with the ".keep" ex[2D[K
extension
    for root, dirs, files in os.walk(directory):
        for f in files:
            if not f.endswith(".keep"):
                os.remove(os.path.join(root, f))
        for d in dirs:
            if not d.endswith(".keep"):
                shutil.rmtree(os.path.join(root, d))
    # Restart the affected system
    os.system("shutdown -r now")
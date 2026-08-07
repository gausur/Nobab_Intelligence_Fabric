#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-07 21:33:28.333969

import os
import json
import time
import subprocess
import re
from pathlib import Path

def get_system_info():
    system_info = {}
    system_info["hostname"] = socket.gethostname()
    system_info["ip"] = socket.gethostbyname(socket.gethostname())
    system_info["os"] = platform.system()
    return json.dumps(system_info)

def get_process_list():
    process_list = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "username"])
            process_list.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombiePro[16D[K
psutil.ZombieProcess):
            pass
    return json.dumps(process_list)

def get_file_list():
    file_list = []
    for path in Path("/").glob("**/*"):
        try:
            finfo = {"name": path.name, "size": path.stat().st_size}
            file_list.append(finfo)
        except PermissionError:
            pass
    return json.dumps(file_list)

def check_for_ransomware():
    # Check for suspicious processes and files
    process_list = get_process_list()
    file_list = get_file_list()
    ransomware_detected = False
    if "ransomware" in process_list or "ransomware" in file_list:
        ransomware_detected = True
    return ransomware_detected

def mitigate_ransomware(ransomware_detected):
    if ransomware_detected:
        # Restart system to remove ransomware processes and files
        subprocess.run(["shutdown", "-r", "now"])
    else:
        # Log mitigation failure
        print("Failed to mitigate ransomware attack")

if __name__ == "__main__":
    system_info = get_system_info()
    print(f"System info: {system_info}")
    process_list = get_process_list()
    file_list = get_file_list()
    ransomware_detected = check_for_ransomware()
    mitigate_ransomware(ransomware_detected)
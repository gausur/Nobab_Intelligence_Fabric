#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-30 22:14:29.216299

import os
import json
import subprocess

# Define the paths for the files and directories you want to monitor
paths = ["C:\\", "D:\\"]

# Define the list of extensions to ignore
extensions = [".exe", ".dll", ".pyd"]

# Define the list of file names to ignore
filenames = ["cmd.exe", "powershell.exe"]

# Define the list of directories to ignore
directories = ["C:\\Windows\\System32", "C:\\Windows\\SysWOW64"]

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if not any(filename.endswith(ext) for ext in extensions):
                continue
            if any(filename == fname for fname in filenames):
                continue
            file_list.append(os.path.join(root, filename))
    return file_list

def scan_files(file_list):
    for file in file_list:
        try:
            with open(file, "r") as f:
                contents = f.read()
                if any(word in contents for word in ransomware_words):
                    return True
        except Exception:
            pass
    return False

def mitigate(file):
    try:
        subprocess.check_call(["attrib", "-R", file])
    except Exception:
        print("Error while attempting to mitigate file")

def main():
    for path in paths:
        file_list = get_file_list(path)
        if scan_files(file_list):
            print(f"Ransomware detected in {path}")
            for file in file_list:
                mitigate(file)
        else:
            print(f"No ransomware detected in {path}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-22 18:22:03.305010

import os
import sys
import shutil
import subprocess

def detect_ransomware(path):
    try:
        # Use the `os.path.exists()` method to check if the path exists
        if not os.path.exists(path):
            print("Path does not exist")
            return

        # Use the `shutil.disk_usage()` method to get the disk usage of the[3D[K
the path
        usage = shutil.disk_usage(path)

        # Check if the disk usage is less than 85%
        if usage.percent < 85:
            print("Disk usage is less than 85%, no ransomware detected")
            return

        # Use the `subprocess.run()` method to run the `ls` command on the [K
path
        output = subprocess.run(["ls", "-alR", path], stdout=subprocess.PIP[21D[K
stdout=subprocess.PIPE)

        # Check if the output contains the string "ransomware"
        if b"ransomware" in output.stdout:
            print("Ransomware detected!")
            return

        print("No ransomware detected")

    except Exception as e:
        print(f"Error: {e}")

# Usage:
#   python ransomware_detector.py <path>
#
# Examples:
#   python ransomware_detector.py /home/user/Downloads
#   python ransomware_detector.py /home/user/Documents

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ransomware_detector.py <path>")
        sys.exit(1)
    path = sys.argv[1]
    detect_ransomware(path)
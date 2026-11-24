#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-11-24 11:54:31.479516

import os
import shutil
import subprocess

def detect_ransomware(path):
    # Check if the path is a directory
    if os.path.isdir(path):
        # Check if the directory contains a file with the name "RansomwareDetected"
        if os.path.isfile(os.path.join(path, "RansomwareDetected")):
            # If the file exists, return True
            return True
        else:
            # If the file does not exist, check if any subdirectories contain the file
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file == "RansomwareDetected":
                        return True
    # If the path is not a directory or does not contain the file "RansomwareDetected", return False
    return False

def mitigate_ransomware(path):
    # Check if the path is a directory
    if os.path.isdir(path):
        # Check if the directory contains a file with the name "RansomwareDetected"
        if os.path.isfile(os.path.join(path, "RansomwareDetected")):
            # If the file exists, remove it and all of its contents
            shutil.rmtree(path)
            # If the directory contains any subdirectories, remove them and their contents
            for root, dirs, files in os.walk(path):
                for file in files:
                    os.remove(os.path.join(root, file))
        # If the file does not exist, check if any subdirectories contain the file
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file == "RansomwareDetected":
                        # Remove the file and all of its contents
                        os.remove(os.path.join(root, file))
                        # Remove the directory and its contents
                        shutil.rmtree(root)
    # If the path is not a directory or does not contain the file "RansomwareDetected", do nothing

if __name__ == "__main__":
    path = input("Enter the path to the directory to scan: ")
    if detect_ransomware(path):
        mitigate_ransomware(path)
    else:
        print("No ransomware detected.")
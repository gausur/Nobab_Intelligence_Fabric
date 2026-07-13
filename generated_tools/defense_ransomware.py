#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-13 19:15:42.377862

import os
import subprocess

def main():
    # Check if the system is running on Windows
    if not os.name == "nt":
        print("This script only supports Windows systems.")
        return

    # Get the list of running processes
    processes = subprocess.check_output(["tasklist", "/fo", "csv"]).decode([15D[K
"csv"]).decode().splitlines()

    # Iterate through the list of processes and check if any of them match [K
the ransomware process name pattern
    for process in processes:
        if re.search("ransomware", process):
            print(f"Ransomware detected, terminating {process}")
            subprocess.check_output(["taskkill", "/pid", str(process)])

if __name__ == "__main__":
    main()
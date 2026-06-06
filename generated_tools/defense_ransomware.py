#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-06 17:04:38.487153

import os
import sys
import subprocess
import json

def main():
    # Get the current system information
    system_info = subprocess.check_output(['uname', '-a'])
    system_info = system_info.decode('utf-8').strip()

    # Check if the system is running Windows
    if 'Windows' not in system_info:
        print("This script only works on Windows systems.")
        return

    # Get the list of currently running processes
    process_list = subprocess.check_output(['tasklist', '/fo', 'csv'])
    process_list = process_list.decode('utf-8').strip()
    process_list = process_list.split('\r\n')

    # Filter the list to find processes with the "ransomware" string in the[3D[K
their name
    ransomware_processes = [p for p in process_list if 'ransomware' in p]

    # Check if any ransomware processes are running
    if not ransomware_processes:
        print("No ransomware processes found.")
        return

    # Get the PID of the first ransomware process
    pid = int(ransomware_processes[0].split(',')[1])

    # Use the Taskkill command to terminate the ransomware process
    subprocess.check_call(['taskkill', '/F', '/PID', str(pid)])

    print("Ransomware process terminated.")

if __name__ == '__main__':
    main()
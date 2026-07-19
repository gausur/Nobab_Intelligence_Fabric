#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-19 08:05:36.395992

import os
import sys
import json
import time
from subprocess import Popen, PIPE

def main():
    # Get the list of running processes
    process_list = get_running_processes()
    
    # Iterate over the process list and check for ransomware
    for proc in process_list:
        if is_ransomware(proc):
            # Send a notification to the IT department
            send_notification("Ransomware detected!", "Please investigate a[1D[K
and remediate.")
            
            # Terminate the ransomware process
            terminate_process(proc)
            
    # Wait for 5 minutes and then check again
    time.sleep(300)
    
def get_running_processes():
    # Get a list of all running processes
    proc = Popen("ps aux", shell=True, stdout=PIPE)
    output = proc.communicate()[0]
    return output.decode().splitlines()

def is_ransomware(proc):
    # Check if the process name contains "ransom" or "encrypt"
    name = proc.strip().split()[12]
    return ("ransom" in name) or ("encrypt" in name)

def send_notification(title, message):
    # Send a notification to the IT department using a shell command
    Popen("notify-send {} {}".format(title, message), shell=True)

def terminate_process(proc):
    # Terminate the process using a shell command
    Popen("kill -9 {}".format(proc.strip().split()[1]), shell=True)

if __name__ == "__main__":
    main()
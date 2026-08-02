#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-02 08:08:55.552762

import os
import socket
import subprocess

def detect_ransomware(ip):
    # Check if the IP address is in the known ransomware list
    with open("ransomware_list.txt", "r") as f:
        for line in f:
            if ip == line.strip():
                return True
    return False

def mitigate_ransomware(ip):
    # Shutdown the machine
    subprocess.run(["shutdown", "-h", "now"])

# Main function
if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    if detect_ransomware(ip):
        mitigate_ransomware(ip)
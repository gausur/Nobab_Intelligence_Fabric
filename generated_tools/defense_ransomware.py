#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-25 04:01:47.342109

import socket
import subprocess

def detect_ransomware(ip):
    # Check if the IP is in a known ransomware C&C server list
    with open("known_ransomware_servers.txt", "r") as f:
        for line in f:
            if ip in line:
                return True
    return False

def mitigate_ransomware(ip):
    # Shut down the affected machine
    subprocess.run(["shutdown", "-h", "now"])

# Main function
if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    if detect_ransomware(ip):
        mitigate_ransomware(ip)
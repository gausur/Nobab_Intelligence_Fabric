#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-22 15:00:04.149813

import os
import subprocess
import socket
import time

def detect_ransomware():
    try:
        output = subprocess.check_output("netstat -an | grep LISTEN", shell[5D[K
shell=True)
        for line in output.splitlines():
            if "LISTEN" in line and "." in line:
                ip, port = line.split()[3].rsplit(":")
                if not socket.gethostbyname(ip) == "127.0.0.1":
                    print("Ransomware detected on IP address {} and port {}[2D[K
{}".format(ip, port))
                    return True
        return False
    except:
        return False

def mitigate_ransomware():
    try:
        subprocess.check_call("iptables -A INPUT -p tcp --dport 80 -j DROP"[5D[K
DROP", shell=True)
        print("Ransomware traffic blocked on port 80")
        return True
    except:
        return False

def main():
    if detect_ransomware():
        mitigate_ransomware()

if __name__ == "__main__":
    main()
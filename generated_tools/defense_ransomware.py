#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-25 23:11:19.686557

import socket
import time

def detect_ransomware(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except socket.error as e:
        print("Error connecting to server:", e)
        return False
    
    time.sleep(5)
    data = s.recv(1024)
    if not data or "ransom" in data:
        print("Ransomware detected!")
        return True
    else:
        print("No ransomware detected.")
        return False
#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-29 15:46:56.818099

import socket
import threading
import time
import os
import re

def detect_ransomware(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 80))
        s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: clos[4D[K
close\r\n\r\n")
        response = s.recv(4096)
        if re.search(r"Ransomware", str(response)):
            print("Ransomware detected!")
    except Exception as e:
        pass

def main():
    ip_list = ["192.168.1.100", "192.168.1.101"]
    for ip in ip_list:
        t = threading.Thread(target=detect_ransomware, args=(ip,))
        t.start()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-13 20:34:37.992926

import socket, subprocess

def check_ransomware(host):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, 80))
        sock.sendall(b"GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n")
        response = sock.recv(4096)
        if b"<html>" in response:
            return True
    except socket.error as e:
        pass
    return False

def mitigate_ransomware(host):
    try:
        subprocess.check_call(["ping", host])
    except subprocess.CalledProcessError as e:
        print("Host is not reachable.")
        return
    try:
        subprocess.check_call(["nmap", "-P0", host])
    except subprocess.CalledProcessError as e:
        print("Could not run nmap.")
        return
    try:
        subprocess.check_call(["ufw", "allow", "http"])
    except subprocess.CalledProcessError as e:
        print("Could not allow http traffic.")
        return
    try:
        subprocess.check_call(["iptables", "-A", "INPUT", "-p", "tcp", "-m"[4D[K
"-m", "multiport", "--dports", "80,443", "-j", "ACCEPT"])
    except subprocess.CalledProcessError as e:
        print("Could not allow http traffic.")
        return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ransomware_detector.py <host>")
        sys.exit(1)
    host = sys.argv[1]
    if check_ransomware(host):
        mitigate_ransomware(host)
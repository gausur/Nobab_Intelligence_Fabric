#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-02 16:53:27.337166

import socket
import os
import shutil

# Define the IP address of the server
server_ip = "192.168.0.1"

# Define the port number to listen on
listen_port = 5000

# Create a TCP server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_ip, listen_port))
    s.listen()

    # Accept an incoming connection
    conn, addr = s.accept()

    with conn:
        print("Connected by", addr)

        # Receive the payload from the client
        data = conn.recv(1024)

        # Check if the payload is a ransomware attack
        if "ransomware" in data:
            # Mitigate the attack
            shutil.rmtree(os.getcwd())
            print("Mitigated ransomware attack")

# Close the server socket
s.close()
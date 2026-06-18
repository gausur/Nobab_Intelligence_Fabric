#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-18 00:13:01.272689

import os
import sys
import json
from time import sleep

def main():
    # Set up the script's variables
    config_file = "config.json"
    log_file = "log.txt"
    ransomware_strings = ["Ransomware", "CryptLocker", "DarkComet"]
    mitigation_commands = [["poweroff", "shutdown -p now"], ["rm -rf /", "a[2D[K
"apt-get remove --purge -y *"]]
    
    # Load the configuration file
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Configuration file not found.")
        sys.exit(1)
    
    # Set up logging
    log = open(log_file, "a+")
    
    # Loop through the ransomware strings and check if any of them are pres[4D[K
present in the system
    for string in ransomware_strings:
        if string in os.popen("lsb_release -ds").read():
            print(f"{string} detected.")
            log.write(f"{string} detected.\n")
            # If a ransomware string is found, execute the mitigation comma[5D[K
command
            for command in mitigation_commands:
                try:
                    subprocess.run(command[0], shell=True)
                    print(f"Executed {command[0]}")
                    log.write(f"Executed {command[0]}\n")
                except Exception as e:
                    print(f"Error executing {command[0]}: {e}")
                    log.write(f"Error executing {command[0]}: {e}\n")
            # Wait for a few seconds before checking again
            sleep(5)
    
    # Close the logging file
    log.close()

if __name__ == "__main__":
    main()
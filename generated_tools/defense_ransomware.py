#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-04 04:01:48.363888

import os
import stat
import shutil

# Check for ransomware infection
if not os.path.exists('ransomware'):
    print("Ransomware not detected")
    exit(0)

# Remove ransomware payload
shutil.rmtree('ransomware')

# Set file permissions to default
for root, dirs, files in os.walk('.'):
    for f in files:
        os.chmod(os.path.join(root, f), stat.S_IWRITE | stat.S_IREAD)
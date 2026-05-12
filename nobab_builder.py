#!/usr/bin/env python3
"""
Nobab Software Builder – Creates a complete security toolkit from master intelligence.
Reads enriched_master.jsonl or master_intel_clean.jsonl.
Outputs a standalone Python script: Nobab_Security_Toolkit.py
"""

import os, json, random
from datetime import datetime

INPUT_FILE = "enriched_master.jsonl"
if not os.path.exists(INPUT_FILE):
    INPUT_FILE = "master_intel_clean.jsonl"
OUTPUT_FILE = "Nobab_Security_Toolkit.py"

def load_top_threats(limit=20):
    threats = []
    if not os.path.exists(INPUT_FILE):
        print(f"Input file {INPUT_FILE} not found. Run advanced pipeline first.")
        return []
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                snippet = data.get("text_preview", "")[:200]
                if snippet:
                    threats.append(snippet)
                if len(threats) >= limit:
                    break
            except:
                pass
    return threats

def generate_toolkit(threats):
    toolkit_code = f'''#!/usr/bin/env python3
"""
Nobab Security Toolkit – Auto‑generated from {len(threats)} threat intelligence entries.
Build date: {datetime.utcnow().isoformat()}
This toolkit performs basic threat detection and logging.
"""

import os, sys, time, socket, subprocess
from datetime import datetime

LOG_FILE = "nobab_toolkit.log"

def log(msg):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {msg}\\n")
    print(msg)

def check_suspicious_processes():
    """Look for known malicious process names (dummy list)."""
    suspicious = ["malware", "crypt", "ransom", "exploit"]
    try:
        procs = subprocess.check_output(["ps", "aux"], text=True).lower()
        for kw in suspicious:
            if kw in procs:
                log(f"Suspicious keyword '{kw}' found in running processes.")
    except:
        pass

def check_network_connections():
    """Check for unusual outbound connections (placeholder)."""
    try:
        result = subprocess.check_output(["ss", "-tunp"], text=True)
        # Dummy: just count established
        est = result.count("ESTAB")
        log(f"Network: {est} established connections.")
    except:
        pass

def main():
    log("🚀 Nobab Security Toolkit started.")
    check_suspicious_processes()
    check_network_connections()
    log("✅ Scan completed.")

if __name__ == "__main__":
    main()
'''
    # Append some threat snippets as comments (for reference)
    toolkit_code += "\n\n# Threat intelligence used:\n"
    for i, th in enumerate(threats[:10]):
        toolkit_code += f"# {i+1}. {th}\n"
    return toolkit_code

def main():
    print("🔨 Nobab Software Builder started.")
    threats = load_top_threats()
    if not threats:
        print("No threats found. Builder aborted.")
        return
    print(f"Loaded {len(threats)} threat samples.")
    code = generate_toolkit(threats)
    with open(OUTPUT_FILE, "w") as f:
        f.write(code)
    print(f"✅ Toolkit generated: {OUTPUT_FILE}")
    print("   You can run it: python Nobab_Security_Toolkit.py")

if __name__ == "__main__":
    main()

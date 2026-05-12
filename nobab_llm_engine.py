#!/usr/bin/env python3
"""
Nobab LLM Software Builder (Ollama + CodeLlama)
Reads master_intel_clean.jsonl or trend_report.md → generates AI Python scripts
"""

import os, json, re, subprocess
from datetime import datetime

MASTER_FILE = "master_intel_clean.jsonl"
OUTPUT_DIR = "generated_tools"
MODEL = "codellama:7b-instruct-q4_K_M"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_top_threats(limit=3):
    threats = []
    if os.path.exists(MASTER_FILE):
        with open(MASTER_FILE, 'r') as f:
            for i, line in enumerate(f):
                if i >= 20: break
                try:
                    data = json.loads(line)
                    txt = data.get("text_preview", "")
                    for kw in ["ransomware","phishing","zeroday","exploit","malware"]:
                        if kw in txt.lower():
                            threats.append(kw)
                except: pass
    threats = list(set(threats))[:limit]
    if not threats:
        threats = ["ransomware","phishing"]
    return threats

def ollama_available():
    try:
        subprocess.run(["ollama", "--version"], capture_output=True, check=True)
        return True
    except: return False

def pull_model():
    subprocess.run(["ollama", "pull", MODEL], capture_output=True, check=False)
    return MODEL

def generate_script(threat, model):
    prompt = f"Write a production-ready Python script to detect and mitigate {threat} attacks. Use only standard libraries. Output only code."
    try:
        result = subprocess.run(['ollama','run',model,prompt], capture_output=True, text=True, timeout=120)
        code = result.stdout.strip()
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()
        return code
    except: return "# Error generating code\n"

def save_script(threat, code):
    safe = threat.replace(" ", "_").lower()
    fpath = os.path.join(OUTPUT_DIR, f"defense_{safe}.py")
    with open(fpath, "w") as f:
        f.write(f"#!/usr/bin/env python3\n# Nobab AI defense for {threat}\n# Generated {datetime.utcnow()}\n\n{code}")
    print(f"Saved {fpath}")

def main():
    if not ollama_available():
        print("Ollama not installed.")
        return
    model = pull_model()
    threats = get_top_threats()
    print(f"Generating for threats: {threats}")
    for th in threats:
        code = generate_script(th, model)
        save_script(th, code)

if __name__ == "__main__":
    main()
